import os
import django
from django.test import TestCase, Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings')
django.setup()

from doubts.models import Subject
from flashcards.models import FlashcardDeck, StudentNote

class FlashcardsAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.phys_subject, _ = Subject.objects.get_or_create(
            code="PHYS",
            defaults={
                "name": "Physics",
                "description": "Physics Mechanics",
                "color_hex": "#EC4899"
            }
        )
        self.deck, _ = FlashcardDeck.objects.get_or_create(
            title="Kinematics Rules Deck",
            defaults={"subject": self.phys_subject}
        )

    def test_deck_list(self):
        res = self.client.get('/api/flashcards/decks/')
        self.assertEqual(res.status_code, 200)

    def test_create_note(self):
        payload = {
            'title': 'Kinematics Formulas Note',
            'content_markdown': '# v = u + at',
            'subject_code': 'PHYS'
        }
        res = self.client.post(
            '/api/flashcards/notes/',
            data=payload,
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
