from django.test import TestCase, Client
from doubts.models import Subject, Doubt, SolutionStep

class DoubtsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.math_subject, _ = Subject.objects.get_or_create(
            code="MATH",
            defaults={
                "name": "Mathematics",
                "description": "Pure and Applied Mathematics",
                "color_hex": "#2563EB"
            }
        )
        self.doubt, _ = Doubt.objects.get_or_create(
            title="How to integrate x*sin(x)?",
            defaults={
                "question_text": "Find the indefinite integral of x * sin(x) dx using integration by parts.",
                "subject": self.math_subject,
                "difficulty": "MEDIUM",
                "student_name": "Alex"
            }
        )

    def test_doubt_list_api(self):
        response = self.client.get('/api/doubts/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')

    def test_doubt_filter_by_subject(self):
        response = self.client.get('/api/doubts/?subject=MATH')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')

    def test_doubt_upvote(self):
        initial_upvotes = self.doubt.upvotes
        response = self.client.post(f'/api/doubts/{self.doubt.id}/upvote/')
        self.assertEqual(response.status_code, 200)
        self.doubt.refresh_from_db()
        self.assertEqual(self.doubt.upvotes, initial_upvotes + 1)
