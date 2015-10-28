from django.http import HttpResponse
from django.template import loader
from django.views import generic
from madNotes.models import Note, Tags
from madNotes import models
from .forms import NoteForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView



def index(request):

    return render(request,"main.html")

class NoteCreate(CreateView):
    model = Note

    fields = ["title", "note", "tags"]
    template_name = "add_note.html"


def home(request):
    notes = Note.objects
    template = loader.get_template('home.html')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    context = {'notes': notes, 'form': form}
    return render(request, template, context)
    #return render_to_response("note.html", notes)

"""display notes on note homepage"""

class NoteIndex(generic.ListView):
    context_object_name = "notes"
    queryset = models.Note.objects.all()
    template_name = "home.html"
    paginate_by = 5


"""displaying the details of a selected note"""
class NoteDetail(generic.DetailView):
    model = Note
    template_name =  "post.html"