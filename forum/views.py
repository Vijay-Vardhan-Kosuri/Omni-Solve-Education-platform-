import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q
from .models import ForumQuestion, ForumAnswer, ForumComment
from doubts.models import Subject

@method_decorator(csrf_exempt, name='dispatch')
class ForumQuestionListView(View):
    def get(self, request):
        query = request.GET.get('q', '').strip()
        subject_code = request.GET.get('subject', '').strip().upper()
        
        qs = ForumQuestion.objects.prefetch_related('answers', 'answers__comments').select_related('subject').all().order_by('-created_at')

        if subject_code:
            qs = qs.filter(subject__code=subject_code)
        if query:
            qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__icontains=query))

        questions_data = []
        for q in qs[:50]:
            questions_data.append({
                'id': q.id,
                'title': q.title,
                'content': q.content,
                'author_name': q.author_name,
                'subject': q.subject.name,
                'subject_code': q.subject.code,
                'subject_color': q.subject.color_hex,
                'tags': [t.strip() for t in q.tags.split(',') if t.strip()],
                'upvotes': q.upvotes,
                'views_count': q.views_count,
                'is_solved': q.is_solved,
                'answers_count': q.answers.count(),
                'created_at': q.created_at.strftime('%Y-%m-%d %H:%M'),
                'answers': [
                    {
                        'id': ans.id,
                        'content': ans.content,
                        'author_name': ans.author_name,
                        'is_accepted': ans.is_accepted,
                        'upvotes': ans.upvotes,
                        'created_at': ans.created_at.strftime('%Y-%m-%d %H:%M'),
                        'comments': [
                            {
                                'author_name': c.author_name,
                                'comment_text': c.comment_text,
                                'created_at': c.created_at.strftime('%Y-%m-%d %H:%M')
                            } for c in ans.comments.all()
                        ]
                    } for ans in q.answers.all()
                ]
            })

        return JsonResponse({'status': 'success', 'count': len(questions_data), 'questions': questions_data})

    def post(self, request):
        try:
            payload = json.loads(request.body.decode('utf-8'))
            title = payload.get('title', '').strip()
            content = payload.get('content', '').strip()
            author_name = payload.get('author_name', 'Student').strip() or 'Student'
            subject_code = payload.get('subject_code', 'MATH').upper()
            tags = payload.get('tags', '').strip()

            if not title or not content:
                return JsonResponse({'status': 'error', 'message': 'Title and content are required'}, status=400)

            subject = Subject.objects.filter(code=subject_code).first()
            if not subject:
                subject = Subject.objects.first()

            question = ForumQuestion.objects.create(
                title=title,
                content=content,
                author_name=author_name,
                subject=subject,
                tags=tags
            )

            return JsonResponse({'status': 'success', 'message': 'Question posted to community forum!', 'id': question.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class ForumAnswerCreateView(View):
    def post(self, request, question_id):
        try:
            payload = json.loads(request.body.decode('utf-8'))
            content = payload.get('content', '').strip()
            author_name = payload.get('author_name', 'Peer Helper').strip() or 'Peer Helper'

            if not content:
                return JsonResponse({'status': 'error', 'message': 'Answer content cannot be empty'}, status=400)

            question = ForumQuestion.objects.get(id=question_id)
            answer = ForumAnswer.objects.create(
                question=question,
                content=content,
                author_name=author_name
            )

            return JsonResponse({'status': 'success', 'message': 'Answer added successfully!', 'answer_id': answer.id})
        except ForumQuestion.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Question not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
