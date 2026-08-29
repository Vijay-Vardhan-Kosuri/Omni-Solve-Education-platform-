import os
import django
from django.test import TestCase, Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings')
django.setup()

from doubts.models import Subject
from flashcards.models import FlashcardDeck, Flashcard, StudentNote

class FlashcardsAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.phys_subject = Subject.objects.create(
            name="Physics",
            code="PHYS",
            description="Physics Mechanics",
            color_hex="#EC4899"
        )
        self.deck = FlashcardDeck.objects.create(
            title="Kinematics Rules",
            subject=self.phys_subject
        )
        Flashcard.objects.create(
            deck=self.deck,
            front_prompt="Newton 2nd Law?",
            back_solution="F = m * a"
        )

    def test_deck_list(self):
        res = self.client.get('/api/flashcards/decks/')
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(len(data['decks']), 1)

    def test_create_note(self):
        payload = {
            'title': 'Kinematics Formulas',
            'content_markdown': '# v = u + at',
            'subject_code': 'PHYS'
        }
        res = self.client.post(
            '/api/flashcards/notes/',
            data=payload,
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(StudentNote.objects.count(), 1)
