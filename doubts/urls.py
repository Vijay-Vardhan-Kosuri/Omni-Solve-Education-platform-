from django.urls import path
from .views import DoubtListView, DoubtDetailView, DoubtUpvoteView

urlpatterns = [
    path('', DoubtListView.as_view(), name='doubt_list'),
    path('<int:doubt_id>/', DoubtDetailView.as_view(), name='doubt_detail'),
    path('<int:doubt_id>/upvote/', DoubtUpvoteView.as_view(), name='doubt_upvote'),
]
