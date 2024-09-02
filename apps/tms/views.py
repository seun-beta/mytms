from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from apps.tms.models import Campaign, Member, Task
from apps.tms.serializers import (
    CampaignSerializer,
    MemberSerializer,
    TaskListSerializer,
    TaskSerializer,
    CreateTaskSerializer,
)
from apps.utility.filters import TaskFilter
from apps.utility.pagination import TaskPagination


class CampaignViewSet(ModelViewSet):
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()


class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    lookup_field = "email"


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all().select_related("campaign", "reviewer", "trainer")
    http_method_names = ["get", "head", "delete", "put"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        breakpoint()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class CreateTaskView(CreateAPIView):
    serializer_class = CreateTaskSerializer
    queryset = Task.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class TaskListView(ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all().select_related("campaign", "reviewer", "trainer")
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
