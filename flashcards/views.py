import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import FlashcardDeck, Flashcard, StudentNote, SavedWhiteboard
from doubts.models import Subject

@method_decorator(csrf_exempt, name='dispatch')
class FlashcardDeckListView(View):
    def get(self, request):
        subject_code = request.GET.get('subject', '').strip().upper()
        qs = FlashcardDeck.objects.prefetch_related('cards').select_related('subject').all()

        if subject_code:
            qs = qs.filter(subject__code=subject_code)

        data = []
        for deck in qs:
            data.append({
                'id': deck.id,
                'title': deck.title,
                'description': deck.description,
                'subject': deck.subject.name,
                'subject_code': deck.subject.code,
                'subject_color': deck.subject.color_hex,
                'cards_count': deck.cards.count(),
                'cards': [
                    {
                        'id': c.id,
                        'front_prompt': c.front_prompt,
                        'back_solution': c.back_solution,
                        'hint': c.hint,
                        'mastery_level': c.mastery_level
                    } for c in deck.cards.all()
                ]
            })

        return JsonResponse({'status': 'success', 'decks': data})

@method_decorator(csrf_exempt, name='dispatch')
class StudentNoteView(View):
    def get(self, request):
        notes = StudentNote.objects.select_related('subject').all().order_by('-updated_at')
        data = [
            {
                'id': n.id,
                'title': n.title,
                'content_markdown': n.content_markdown,
                'subject': n.subject.name,
                'subject_code': n.subject.code,
                'tags': [t.strip() for t in n.tags.split(',') if t.strip()],
                'updated_at': n.updated_at.strftime('%Y-%m-%d %H:%M')
            } for n in notes
        ]
        return JsonResponse({'status': 'success', 'notes': data})

    def post(self, request):
        try:
            payload = json.loads(request.body.decode('utf-8'))
            title = payload.get('title', '').strip()
            content = payload.get('content_markdown', '').strip()
            subject_code = payload.get('subject_code', 'MATH').upper()
            tags = payload.get('tags', '').strip()

            if not title or not content:
                return JsonResponse({'status': 'error', 'message': 'Title and content are required'}, status=400)

            subject = Subject.objects.filter(code=subject_code).first() or Subject.objects.first()
            note = StudentNote.objects.create(
                title=title,
                content_markdown=content,
                subject=subject,
                tags=tags
            )

            return JsonResponse({'status': 'success', 'message': 'Note saved!', 'note_id': note.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class SavedWhiteboardView(View):
    def get(self, request):
        boards = SavedWhiteboard.objects.all().order_by('-created_at')[:20]
        data = [
            {
                'id': b.id,
                'title': b.title,
                'canvas_json': b.canvas_json_data,
                'created_at': b.created_at.strftime('%Y-%m-%d %H:%M')
            } for b in boards
        ]
        return JsonResponse({'status': 'success', 'whiteboards': data})

    def post(self, request):
        try:
            payload = json.loads(request.body.decode('utf-8'))
            title = payload.get('title', 'Scratchpad Diagram').strip()
            canvas_json = payload.get('canvas_json', '{}').strip()

            wb = SavedWhiteboard.objects.create(
                title=title,
                canvas_json_data=canvas_json
            )
            return JsonResponse({'status': 'success', 'message': 'Whiteboard saved!', 'id': wb.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
