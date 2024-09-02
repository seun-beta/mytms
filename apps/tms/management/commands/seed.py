from django.core.management.base import BaseCommand, CommandError
from apps.tms.models import Campaign, Member, Task


class Command(BaseCommand):
    help = "Create seed data for TMS "

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS("Successfully seeded data"))
