from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<int:pk>", views.PostDetailView.as_view(), name="detail"),
    path("create/", views.PostCreateView.as_view(), name="create"),
]