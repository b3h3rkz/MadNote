from django.http import HttpResponse
from django.template import loader
from django.views import generic
from madNotes.models import Note, Tags
from madNotes import models
from .forms import NoteForm, TagForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView



def index(request):
    return render(request,"home.html")

class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "add_note.html"
    success_url = "/notes"


"""display notes on note homepage"""


class NoteIndex(generic.ListView):
    context_object_name = "notes"
    queryset = models.Note.objects.all()
    template_name = "home.html"
    paginate_by = 5


"""displaying the details of a selected note"""


class NoteDetail(generic.DetailView):
    model = Note
    template_name = "detail.html"
