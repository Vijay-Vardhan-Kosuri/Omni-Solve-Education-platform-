from django.contrib import admin
from .models import ForumQuestion, ForumAnswer, ForumComment

@admin.register(ForumQuestion)
class ForumQuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'author_name', 'upvotes', 'is_solved', 'created_at')
    list_filter = ('subject', 'is_solved')
    search_fields = ('title', 'content', 'tags')

@admin.register(ForumAnswer)
class ForumAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author_name', 'is_accepted', 'upvotes', 'created_at')

@admin.register(ForumComment)
class ForumCommentAdmin(admin.ModelAdmin):
    list_display = ('answer', 'author_name', 'created_at')
