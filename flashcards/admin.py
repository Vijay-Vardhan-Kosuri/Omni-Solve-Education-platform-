from django.contrib import admin
from .models import FlashcardDeck, Flashcard, StudentNote, SavedWhiteboard

class FlashcardInline(admin.TabularInline):
    model = Flashcard
    extra = 1

@admin.register(FlashcardDeck)
class FlashcardDeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'is_public', 'created_at')
    inlines = [FlashcardInline]

@admin.register(StudentNote)
class StudentNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'updated_at')

@admin.register(SavedWhiteboard)
class SavedWhiteboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
