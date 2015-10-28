from django.conf.urls import patterns, include, url
from django.contrib import admin
from MadNotez import settings
from madNotes import views
from madNotes.views import *
from registration.backends.default.views import RegistrationView
from madNotes.forms import ExRegistrationForm
if settings.DEBUG:
    import debug_toolbar
urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'accounts/register/$', RegistrationView.as_view(form_class = ExRegistrationForm), name='registration_register'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include('django_markdown.urls')),
    url('^notes/', include('madNotes.urls')),
    url(r'^', views.index, name='index')



)
