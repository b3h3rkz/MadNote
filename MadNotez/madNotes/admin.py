from django.contrib import admin
from madNotes.models import Note, Tags
from django_markdown.admin import MarkdownModelAdmin


class NotesAdmin(MarkdownModelAdmin):
    list_display = ("title", "created", "modified")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Note, NotesAdmin)
admin.site.register(Tags)
