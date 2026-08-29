import os
import django
from django.test import TestCase, Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings')
django.setup()

from doubts.models import Subject
from forum.models import ForumQuestion, ForumAnswer

class ForumAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.cs_subject = Subject.objects.create(
            name="Computer Science",
            code="CS",
            description="CS & Algorithms",
            color_hex="#10B981"
        )
        self.question = ForumQuestion.objects.create(
            title="BFS vs DFS",
            content="When to use BFS instead of DFS?",
            author_name="Alice",
            subject=self.cs_subject,
            tags="algorithms, graph"
        )

    def test_forum_question_list(self):
        res = self.client.get('/api/forum/questions/')
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data['status'], 'success')

    def test_add_answer(self):
        payload = {'content': 'Use BFS for shortest path.', 'author_name': 'Expert'}
        res = self.client.post(
            f'/api/forum/questions/{self.question.id}/answers/',
            data=payload,
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(self.question.answers.count(), 1)
