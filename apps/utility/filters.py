import django_filters as filters

from apps.tms.models import Task


class TaskFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="created_at", lookup_expr="date__gte")
    end_date = filters.DateFilter(field_name="created_at", lookup_expr="date__lte")

    class Meta:
        model = Task
        fields = [
            "start_date",
            "end_date",
        ]
