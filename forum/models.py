from django.db import models
from doubts.models import Subject

class ForumQuestion(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_name = models.CharField(max_length=100, default='Student')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='forum_questions')
    tags = models.CharField(max_length=200, help_text="Comma-separated tags e.g. calculus, limits, derivatives")
    upvotes = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    is_solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ForumAnswer(models.Model):
    question = models.ForeignKey(ForumQuestion, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    author_name = models.CharField(max_length=100, default='Peer / Educator')
    is_accepted = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)
    latex_support = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer to '{self.question.title[:30]}' by {self.author_name}"

class ForumComment(models.Model):
    answer = models.ForeignKey(ForumAnswer, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100, default='Student')
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
