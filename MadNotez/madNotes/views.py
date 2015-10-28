from django.http import request
from django.views import generic
from django.shortcuts import render, render_to_response, RequestContext
from madNotes.models import Note, Tags
from madNotes import models
from .forms import NoteForm
from django.views.generic.edit import FormView
"""
class NoteView(FormView):
    template_name = "home.html"
    form_class = NoteForm
    success_url = '/'

    def home(request):
        notes = Note.objects.all()
        form = NoteForm(request.POST or None)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save(notes)


        return render(request, 'home.html')

"""

"""display notes on note homepage"""
class NoteIndex(generic.ListView):
    model=Note
    queryset = models.Note.objects.all()
    template_name = "home.html"
    paginate_by = 5


"""displaying the details of a selected note"""
class NoteDetail(generic.DetailView):
    model = models.Note
    template_name =  "details.html"