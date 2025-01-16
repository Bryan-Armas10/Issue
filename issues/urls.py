from django.urls import path
from issues import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("to_do/", views.ToDoPostListView.as_view(), name="to_do"),
    path("in_progress/", views.InProgressPostListView.as_view(), name="in_progress"),
    path("done/", views.DonePostListView.as_view(), name="done"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
]
