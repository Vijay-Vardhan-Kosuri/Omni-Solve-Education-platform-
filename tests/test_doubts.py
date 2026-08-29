import os
import django
from django.test import TestCase, Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings')
django.setup()

from doubts.models import Subject, Doubt, SolutionStep

class DoubtsAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.math_subject = Subject.objects.create(
            name="Mathematics",
            code="MATH",
            description="Pure & Applied Math",
            color_hex="#2563EB"
        )
        self.doubt = Doubt.objects.create(
            title="Integrate x*cos(x)",
            question_text="Evaluate \\int x \\cos(x) dx",
            subject=self.math_subject,
            difficulty="MEDIUM"
        )

    def test_doubt_creation(self):
        self.assertEqual(self.doubt.title, "Integrate x*cos(x)")
        self.assertEqual(self.doubt.subject.code, "MATH")

    def test_doubt_api_list(self):
        res = self.client.get('/api/doubts/')
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data['status'], 'success')

    def test_doubt_upvote(self):
        res = self.client.post(f'/api/doubts/{self.doubt.id}/upvote/')
        self.assertEqual(res.status_code, 200)
        self.doubt.refresh_from_db()
        self.assertEqual(self.doubt.upvotes, 1)
