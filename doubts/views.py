import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q
from .models import Subject, TopicCategory, Doubt, SolutionStep, DoubtFeedback

@method_decorator(csrf_exempt, name='dispatch')
class DoubtListView(View):
    def get(self, request):
        query = request.GET.get('q', '').strip()
        subject_code = request.GET.get('subject', '').strip().upper()
        difficulty = request.GET.get('difficulty', '').strip().upper()

        doubts_qs = Doubt.objects.prefetch_related('steps').select_related('subject', 'category').all()

        if subject_code:
            doubts_qs = doubts_qs.filter(subject__code=subject_code)
        if difficulty:
            doubts_qs = doubts_qs.filter(difficulty=difficulty)
        if query:
            doubts_qs = doubts_qs.filter(
                Q(title__icontains=query) | 
                Q(question_text__icontains=query) |
                Q(latex_formula__icontains=query)
            )

        data = []
        for d in doubts_qs[:50]:
            data.append({
                'id': d.id,
                'title': d.title,
                'question_text': d.question_text,
                'subject': d.subject.name,
                'subject_code': d.subject.code,
                'subject_color': d.subject.color_hex,
                'difficulty': d.difficulty,
                'status': d.status,
                'student_name': d.student_name,
                'views_count': d.views_count,
                'upvotes': d.upvotes,
                'latex_formula': d.latex_formula,
                'code_snippet': d.code_snippet,
                'created_at': d.created_at.strftime('%Y-%m-%d %H:%M'),
                'steps': [
                    {
                        'step_number': step.step_number,
                        'step_title': step.step_title,
                        'explanation': step.explanation,
                        'formula_used': step.formula_used,
                        'code_output': step.code_execution_output
                    } for step in d.steps.all()
                ]
            })

        return JsonResponse({'status': 'success', 'count': len(data), 'doubts': data})

    def post(self, request):
        try:
            payload = json.loads(request.body.decode('utf-8'))
            title = payload.get('title', '').strip()
            question_text = payload.get('question_text', '').strip()
            subject_code = payload.get('subject_code', 'MATH').upper()
            difficulty = payload.get('difficulty', 'MEDIUM').upper()
            student_name = payload.get('student_name', 'Student').strip() or 'Student'
            latex_formula = payload.get('latex_formula', '').strip()
            code_snippet = payload.get('code_snippet', '').strip()

            if not title or not question_text:
                return JsonResponse({'status': 'error', 'message': 'Title and Question text are required.'}, status=400)

            subject = Subject.objects.filter(code=subject_code).first()
            if not subject:
                subject = Subject.objects.first()

            doubt = Doubt.objects.create(
                title=title,
                question_text=question_text,
                subject=subject,
                difficulty=difficulty,
                student_name=student_name,
                latex_formula=latex_formula,
                code_snippet=code_snippet,
                status='SOLVED'
            )

            # Trigger solver engine from knowledge_base app
            from knowledge_base.services import solve_student_doubt
            solution_data = solve_student_doubt(subject_code, title, question_text, latex_formula, code_snippet)

            for idx, s in enumerate(solution_data.get('steps', []), start=1):
                SolutionStep.objects.create(
                    doubt=doubt,
                    step_number=idx,
                    step_title=s.get('title', f'Step {idx}'),
                    explanation=s.get('explanation', ''),
                    formula_used=s.get('formula', ''),
                    code_execution_output=s.get('code_output', '')
                )

            return JsonResponse({
                'status': 'success',
                'message': 'Doubt submitted and resolved successfully!',
                'doubt_id': doubt.id,
                'solution': solution_data
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class DoubtDetailView(View):
    def get(self, request, doubt_id):
        try:
            doubt = Doubt.objects.prefetch_related('steps').select_related('subject').get(id=doubt_id)
            doubt.views_count += 1
            doubt.save(update_fields=['views_count'])

            return JsonResponse({
                'status': 'success',
                'doubt': {
                    'id': doubt.id,
                    'title': doubt.title,
                    'question_text': doubt.question_text,
                    'subject': doubt.subject.name,
                    'subject_code': doubt.subject.code,
                    'difficulty': doubt.difficulty,
                    'student_name': doubt.student_name,
                    'views_count': doubt.views_count,
                    'upvotes': doubt.upvotes,
                    'latex_formula': doubt.latex_formula,
                    'code_snippet': doubt.code_snippet,
                    'created_at': doubt.created_at.strftime('%Y-%m-%d %H:%M'),
                    'steps': [
                        {
                            'step_number': step.step_number,
                            'step_title': step.step_title,
                            'explanation': step.explanation,
                            'formula_used': step.formula_used,
                            'code_output': step.code_execution_output
                        } for step in doubt.steps.all()
                    ]
                }
            })
        except Doubt.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Doubt not found'}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class DoubtUpvoteView(View):
    def post(self, request, doubt_id):
        try:
            doubt = Doubt.objects.get(id=doubt_id)
            doubt.upvotes += 1
            doubt.save(update_fields=['upvotes'])
            return JsonResponse({'status': 'success', 'upvotes': doubt.upvotes})
        except Doubt.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Doubt not found'}, status=404)
