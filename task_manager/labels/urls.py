"""URL routing of the labels app."""

from django.urls import path

from task_manager.labels.views import (
    CreateLabelView,
    main
)

urlpatterns = [
    path('', main, name='labels'),
    path('create/', CreateLabelView.as_view(), name='create_label'),
]
