from django.test import TestCase, Client
from doubts.models import Subject
from flashcards.models import FlashcardDeck, Flashcard, StudentNote

class FlashcardTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.phys_subject = Subject.objects.create(
            name="Physics",
            code="PHYS",
            description="Classical and Modern Physics",
            color_hex="#EC4899"
        )
        self.deck = FlashcardDeck.objects.create(
            title="Newton's Laws & Mechanics",
            subject=self.phys_subject
        )
        Flashcard.objects.create(
            deck=self.deck,
            front_prompt="What is Newton's Second Law of Motion?",
            back_solution="F = m * a (Force equals mass times acceleration)."
        )

    def test_flashcard_deck_list(self):
        response = self.client.get('/api/flashcards/decks/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(len(data['decks']), 1)

    def test_create_student_note(self):
        payload = {
            'title': 'Kinematics Summary',
            'content_markdown': '# Kinematics Equations\n- v = u + at\n- s = ut + 0.5at^2',
            'subject_code': 'PHYS',
            'tags': 'physics, formulas'
        }
        response = self.client.post(
            '/api/flashcards/notes/',
            data=payload,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(StudentNote.objects.count(), 1)
