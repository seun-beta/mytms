from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.tms.views import (
    CampaignViewSet,
    MemberViewSet,
    TaskListView,
    TaskViewSet,
    CreateTaskView,
)

router = DefaultRouter()

router.register(r"campaigns", CampaignViewSet, basename="campaigns")
router.register(r"members", MemberViewSet, basename="members")
router.register(r"tasks", TaskViewSet, basename="tasks")
urlpatterns = [
    path("tms/task-list", TaskListView.as_view(), name="task_list"),
    path("tms/create-task", CreateTaskView.as_view(), name="create_task"),
]
