from django.urls import path
from .views import CodeSubmissionListView, CodeSubmissionDetailView

urlpatterns = [
    path('code-submissions/', CodeSubmissionListView.as_view(),
         name='code-submission-list'),
    path('code-submissions/<int:pk>/', CodeSubmissionDetailView.as_view(),
         name='code-submission-detail'),
]
