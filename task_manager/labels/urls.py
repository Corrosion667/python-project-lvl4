"""URL routing of the labels app."""

from django.urls import path

from task_manager.labels.views import CreateLabelView, UpdateLabelView, main, DeleteLabelView

urlpatterns = [
    path('', main, name='labels'),
    path('create/', CreateLabelView.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateLabelView.as_view(), name='update_label'),
    path('<int:pk>/delete/', DeleteLabelView.as_view(), name='delete_label'),
]
