from django.urls import path

from objectives.api_views import ObjectivesCreateView, ObjectivesListView, ObjectivesUpdateView

urlpatterns = [
    path("", ObjectivesListView.as_view(), name="list_objectives"),
    path("create/", ObjectivesCreateView.as_view(), name="create_objectives"),
    path("<int:pk>/edit/", ObjectivesUpdateView.as_view(), name="edit_objectives"),
]



# api_objectives, api_objective, api_finished_obj, api_cancelled_obj, api_show_all