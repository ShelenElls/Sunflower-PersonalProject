from django.urls import path

from objectives.views import ObjectivesCreateView, ObjectivesListView, ObjectivesUpdateView

urlpatterns = [
    path("", ObjectivesListView.as_view(), name="list_objectives"),
    path("create/", ObjectivesCreateView.as_view(), name="create_objectives"),
    path("<int:pk>/edit/", ObjectivesUpdateView.as_view(), name="edit_objectives"),
]
