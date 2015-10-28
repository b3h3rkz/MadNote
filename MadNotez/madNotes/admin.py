from django.contrib import admin
from madNotes.models import Note, Tags
# Register your models here.

from django_markdown.admin import MarkdownModelAdmin


class NotesAdmin(MarkdownModelAdmin):
    list_display = ("title", "created", "modified")

admin.site.register(Note, NotesAdmin)
admin.site.register(Tags)
