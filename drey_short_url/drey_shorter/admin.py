from django.contrib import admin
from .models import drey_link_saved
from django.contrib.admin.models import LogEntry

#  the following line of code deletes the logs in the admin section
LogEntry.objects.all().delete()
# This line of code allow the admin page to view the database
admin.site.register(drey_link_saved)
