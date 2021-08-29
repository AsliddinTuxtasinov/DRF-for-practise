from django.urls import path
from .views import (
    PostListViews, PostRetrieveDestroyView,
    VoteCreateview
)


urlpatterns = [
    path('posts/', PostListViews.as_view()),
    path('posts/<int:pk>/', PostRetrieveDestroyView.as_view()),
    path('posts/<int:pk>/vote/', VoteCreateview.as_view()),
]