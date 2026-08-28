from django.test import TestCase, Client
from doubts.models import Subject
from forum.models import ForumQuestion, ForumAnswer

class ForumTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.cs_subject = Subject.objects.create(
            name="Computer Science",
            code="CS",
            description="Algorithms and Programming",
            color_hex="#10B981"
        )
        self.question = ForumQuestion.objects.create(
            title="Difference between process and thread?",
            content="Can someone explain the primary differences in memory space between OS processes and threads?",
            author_name="David",
            subject=self.cs_subject,
            tags="os, process, thread"
        )

    def test_forum_question_list(self):
        response = self.client.get('/api/forum/questions/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertGreaterEqual(len(data['questions']), 1)

    def test_forum_add_answer(self):
        payload = {
            'content': 'Processes have separate address spaces, whereas threads share the memory space of their parent process.',
            'author_name': 'Prof. CS'
        }
        response = self.client.post(
            f'/api/forum/questions/{self.question.id}/answers/',
            data=payload,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.question.answers.count(), 1)
