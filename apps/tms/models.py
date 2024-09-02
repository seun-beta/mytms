import uuid

from django.db import models

from apps.utility.base_model import TimeStampedUUIDModel


class Campaign(TimeStampedUUIDModel):
    """
    Campaign model for holding campaign data.

    Attributes:
        id (UUIDField): The unique identifier for the campaign, automatically generated.
        name (CharField): The name of the campaign, which must be unique and can have a maximum length of 512 characters.
    """

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    name = models.CharField(max_length=512, unique=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the Campaign instance.

        Returns:
            str: A string in the format 'Campaign Name: {self.name}'.
        """
        return f"Campaign Name: {self.name}"

    class Meta:
        """
        Meta class for Campaign model.

        Attributes:
            verbose_name_plural (str): The plural name for the model in the admin interface.
            ordering (list): The default ordering for querying the model, which orders by the 'created_at' field in descending order.
        """

        verbose_name_plural = "campaigns"
        ordering = ["-created_at"]


ROLE_CHOICES = {
    "Trainer": "Trainer",
    "Lead": "Lead",
}


class Member(TimeStampedUUIDModel):
    """
    Member model for holding member data.

    Attributes:
        id (UUIDField): The unique identifier for the member, automatically generated.
        email (EmailField): The email address of the member, which must be unique and serves as the primary key.
        full_name (CharField): The full name of the member, which must be unique and can have a maximum length of 512 characters.
        role (CharField): The role of the member, chosen from predefined ROLE_CHOICES. Defaults to 'Trainer'.
        campaign (M2M): The campaign
    """

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True, primary_key=True)
    full_name = models.CharField(max_length=512)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
    )
    campaign = models.ManyToManyField(Campaign)

    def __str__(self) -> str:
        """
        Returns a string representation of the Member instance.

        Returns:
            str: A string in the format 'Member: {self.email} == {self.full_name}'.
        """
        return f"Member: {self.email} == {self.full_name}"

    class Meta:
        """
        Meta class for Member model.

        Attributes:
            verbose_name_plural (str): The plural name for the model in the admin interface.
            ordering (list): The default ordering for querying the model, which orders by the 'created_at' field in descending order.
        """

        verbose_name_plural = "members"
        ordering = ["-created_at"]


STATUS_CHOICES = {
    "IN PROGRESS": "IN PROGRESS",
    "SUBMITTED": "SUBMITTED",
    "REVIEWED": "REVIEWED",
}


class Task(TimeStampedUUIDModel):
    """
    Task model for holding task data.

    Attributes:
        id (UUIDField): The unique identifier for the task, automatically generated.
        name (CharField): The name of the task, which can have a maximum length of 512 characters.
        role (CharField): The role associated with the task, chosen from predefined STATUS_CHOICES.
        score (FloatField): The score associated with the task.
        trainer (FK): The trainer
        reviewer (FK): The reviewer
        campaign (M2M): The campaign
    """

    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    name = models.CharField(max_length=512)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
    )
    score = models.FloatField(null=True)
    trainer = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="trainer"
    )
    reviewer = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="reviewer", null=True
    )
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name="campaign", null=True
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the Task instance.

        Returns:
            str: A string in the format 'Task: {self.name}'.
        """
        return f"Task: {self.name}"

    class Meta:
        """
        Meta class for Task model.

        Attributes:
            verbose_name_plural (str): The plural name for the model in the admin interface.
            ordering (list): The default ordering for querying the model, which orders by the 'created_at' field in descending order.
        """

        verbose_name_plural = "tasks"
        ordering = ["-created_at"]
