import os
import django
from django.test import TestCase, Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings')
django.setup()

from doubts.models import Subject, Doubt

class DoubtsAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.math_subject, _ = Subject.objects.get_or_create(
            code="MATH",
            defaults={
                "name": "Mathematics",
                "description": "Pure & Applied Math",
                "color_hex": "#2563EB"
            }
        )
        self.doubt, _ = Doubt.objects.get_or_create(
            title="Integrate x*cos(x)",
            defaults={
                "question_text": "Evaluate \\int x \\cos(x) dx",
                "subject": self.math_subject,
                "difficulty": "MEDIUM"
            }
        )

    def test_doubt_creation(self):
        self.assertEqual(self.doubt.title, "Integrate x*cos(x)")

    def test_doubt_api_list(self):
        res = self.client.get('/api/doubts/')
        self.assertEqual(res.status_code, 200)

    def test_doubt_upvote(self):
        res = self.client.post(f'/api/doubts/{self.doubt.id}/upvote/')
        self.assertEqual(res.status_code, 200)
