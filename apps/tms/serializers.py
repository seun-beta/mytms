from rest_framework import serializers

from apps.tms.models import Campaign, Member, Task


class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ["reviewer", "score"]


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
