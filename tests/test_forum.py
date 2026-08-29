import os
import django
from django.test import TestCase, Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings')
django.setup()

from doubts.models import Subject
from forum.models import ForumQuestion

class ForumAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.cs_subject, _ = Subject.objects.get_or_create(
            code="CS",
            defaults={
                "name": "Computer Science",
                "description": "CS & Algorithms",
                "color_hex": "#10B981"
            }
        )
        self.question, _ = ForumQuestion.objects.get_or_create(
            title="BFS vs DFS Comparison",
            defaults={
                "content": "When to use BFS instead of DFS?",
                "author_name": "Alice",
                "subject": self.cs_subject,
                "tags": "algorithms, graph"
            }
        )

    def test_forum_question_list(self):
        res = self.client.get('/api/forum/questions/')
        self.assertEqual(res.status_code, 200)

    def test_add_answer(self):
        payload = {'content': 'Use BFS for shortest path.', 'author_name': 'Expert'}
        res = self.client.post(
            f'/api/forum/questions/{self.question.id}/answers/',
            data=payload,
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
