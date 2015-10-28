from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from registration.signals import user_registered
from django_markdown.models import MarkdownField


class Tags(models.Model):
    label = models.CharField(max_length=30, default="", unique=False)

    """method for describing each entry"""
    def __str__(self):
        return self.label


class Note(models.Model):
    title = models.CharField(max_length=50, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    note = models.TextField()
    tags = models.ManyToManyField(Tags, related_name="notes")
    slug = models.SlugField(unique=True, default="")

    note = MarkdownField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Mad Note"
        verbose_name_plural = "Note Entries"
        ordering = ["-created"]


class ExUserProfile(models.Model):
    HUMAN_CHOICES = (
        ('y', 'YES'),
        ('n', ' NO'),
    )

    user = models.ForeignKey(User, unique=True)
    is_human = models.NullBooleanField(default=None, choices=HUMAN_CHOICES)

    def __str__(self):
        return self.user



def user_registered_callback(sender, user, request, **kwargs):
    profile = ExUserProfile(user = user)
    profile.is_human = bool(request.POST["is_human"])
    profile.save()

user_registered.connect(user_registered_callback)