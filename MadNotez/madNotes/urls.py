from django.conf.urls import patterns, url
from . import views
from madNotes.models import Note
from madNotes.views import NoteIndex, NoteCreate


urlpatterns = patterns(
    '',
    url(r'^$', NoteIndex.as_view()),
    url(r'^(?P<slug>\S+)/$', views.NoteDetail.as_view(), name="entry_detail"),
    url(r'^/create/$', NoteCreate.as_view(), name="new note"),


 )
