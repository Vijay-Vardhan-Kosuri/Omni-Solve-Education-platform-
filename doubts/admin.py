from django.contrib import admin
from .models import Subject, TopicCategory, Doubt, SolutionStep, DoubtFeedback

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'color_hex', 'created_at')

@admin.register(TopicCategory)
class TopicCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'slug')

class SolutionStepInline(admin.TabularInline):
    model = SolutionStep
    extra = 1

@admin.register(Doubt)
class DoubtAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'difficulty', 'status', 'upvotes', 'views_count', 'created_at')
    list_filter = ('subject', 'difficulty', 'status')
    search_fields = ('title', 'question_text')
    inlines = [SolutionStepInline]
