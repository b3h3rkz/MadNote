from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.NoteIndex.as_view()),
    url(r'^(?P<description>\S+)$', views.NoteDetail.as_view(), name="note_detail")
)
