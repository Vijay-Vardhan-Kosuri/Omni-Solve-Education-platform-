from django.urls import path
from .views import FlashcardDeckListView, StudentNoteView, SavedWhiteboardView

urlpatterns = [
    path('decks/', FlashcardDeckListView.as_view(), name='flashcard_decks'),
    path('notes/', StudentNoteView.as_view(), name='student_notes'),
    path('whiteboards/', SavedWhiteboardView.as_view(), name='saved_whiteboards'),
]
