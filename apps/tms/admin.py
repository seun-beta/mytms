from django.contrib import admin

from apps.tms.models import Campaign, Member, Task

admin.site.register(Member)
admin.site.register(Campaign)
admin.site.register(Task)
