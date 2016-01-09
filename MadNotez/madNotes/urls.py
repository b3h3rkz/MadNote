from django.conf.urls import patterns, url
from . import views
from madNotes.views import  NoteCreate, NoteIndex, NoteUpdateView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewset)

urlpatterns = patterns(
    '',
    url(r'^add/$', NoteCreate.as_view(), name="new_note"),
    url(r'^$', NoteIndex.as_view()),
    url(r'^(?P<slug>\S+)/$', views.NoteDetail.as_view(), name="entry_detail"),
    url(r'^(?P<slug>[-\w]+)/update$', NoteUpdateView.as_view(), name='recipe-update'),

 )


