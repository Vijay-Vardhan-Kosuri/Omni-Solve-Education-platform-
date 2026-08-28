from django.db import models
from doubts.models import Subject

class FlashcardDeck(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='decks')
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.subject.code})"

class Flashcard(models.Model):
    deck = models.ForeignKey(FlashcardDeck, on_delete=models.CASCADE, related_name='cards')
    front_prompt = models.TextField(help_text="Question, formula or concept on front of card")
    back_solution = models.TextField(help_text="Answer or explanation on back of card")
    hint = models.CharField(max_length=255, blank=True)
    mastery_level = models.IntegerField(default=0, help_text="0 to 5 mastery rating")

    def __str__(self):
        return f"Card #{self.id} in {self.deck.title}"

class StudentNote(models.Model):
    title = models.CharField(max_length=255)
    content_markdown = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='notes')
    tags = models.CharField(max_length=200, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SavedWhiteboard(models.Model):
    title = models.CharField(max_length=200, default='Untitled Diagram')
    canvas_json_data = models.TextField(help_text="JSON payload containing stroke coordinates")
    preview_image_base64 = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
