from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    icon_name = models.CharField(max_length=50, default='book')
    color_hex = models.CharField(max_length=10, default='#3B82F6')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TopicCategory(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Topic Categories"

    def __str__(self):
        return f"{self.subject.code} - {self.name}"

class Doubt(models.Model):
    DIFFICULTY_CHOICES = [
        ('EASY', 'Beginner / Fundamental'),
        ('MEDIUM', 'Intermediate / Standard'),
        ('HARD', 'Advanced / Olympiad'),
    ]

    STATUS_CHOICES = [
        ('SOLVED', 'Solved'),
        ('PENDING', 'Pending Review'),
        ('AI_GENERATED', 'AI / Heuristic Resolved'),
    ]

    title = models.CharField(max_length=300)
    question_text = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='doubts')
    category = models.ForeignKey(TopicCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='doubts')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='MEDIUM')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SOLVED')
    student_name = models.CharField(max_length=100, default='Anonymous Student')
    views_count = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    latex_formula = models.TextField(blank=True, help_text="Optional LaTeX math expression associated with doubt")
    code_snippet = models.TextField(blank=True, help_text="Optional code snippet for CS doubts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.subject.code}] {self.title}"

class SolutionStep(models.Model):
    doubt = models.ForeignKey(Doubt, on_delete=models.CASCADE, related_name='steps')
    step_number = models.PositiveIntegerField()
    step_title = models.CharField(max_length=200)
    explanation = models.TextField()
    formula_used = models.TextField(blank=True)
    diagram_type = models.CharField(max_length=50, blank=True)
    code_execution_output = models.TextField(blank=True)

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.step_title} (Doubt #{self.doubt.id})"

class DoubtFeedback(models.Model):
    doubt = models.ForeignKey(Doubt, on_delete=models.CASCADE, related_name='feedbacks')
    is_helpful = models.BooleanField(default=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
