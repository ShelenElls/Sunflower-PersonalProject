from django.urls import path

from finlit.api_views import ProfileCreateView, ProfileListView, ProfileUpdateView

urlpatterns = [
    path("", ProfileListView.as_view(), name="list_finance"),
    path("create/", ProfileCreateView.as_view(), name="create_finance"),
    path("<int:pk>/edit/", ProfileUpdateView.as_view(), name="edit_finance"),
]
