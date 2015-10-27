from django.views import generic
from madNotes import models

class NoteIndex(generic.ListView):
    queryset = models.Note.objects.all()
    template_name = "home.html"
    paginate_by = 4

class NoteDetail(generic.DetailView):
    model = models.Note
    template_name =  "details.html"