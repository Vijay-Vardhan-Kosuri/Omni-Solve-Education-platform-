from django.urls import path
from .views import ForumQuestionListView, ForumAnswerCreateView

urlpatterns = [
    path('questions/', ForumQuestionListView.as_view(), name='forum_questions'),
    path('questions/<int:question_id>/answers/', ForumAnswerCreateView.as_view(), name='forum_add_answer'),
]
