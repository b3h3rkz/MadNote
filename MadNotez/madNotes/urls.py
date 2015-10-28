from django.conf.urls import patterns, url
from . import views
from madNotes.views import  NoteCreate, NoteIndex



urlpatterns = patterns(
    '',
    url(r'^add/$', NoteCreate.as_view(), name="new_note"),
    url(r'^$', NoteIndex.as_view()),
    url(r'^(?P<slug>\S+)/$', views.NoteDetail.as_view(), name="entry_detail"),

 )
