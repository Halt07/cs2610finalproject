import itertools
from models import Note
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils.text import slugify

class ListView(generic.ListView):
  model = Note
  template_name = 'notes/note_list.html'
  context_object_name = 'notes_list'
  
  
  def get_queryset(self):
      """Return list of notes."""
      return Note.objects.all();

class DetailView(generic.DetailView):
  model = Note
  template_name = 'notes/note_detail.html'
  
def create_note(request):
    error_msg = u"No POST data sent."
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('title'):
                title = post['title']
                new_note = Note.objects.create(title=title)
                return HttpResponseRedirect(new_note.get_absolute_url())
        else:
            error_msg = u"Insufficient Data, Please provide a Note Title.)"
    return HttpResponseServerError(error_msg)
    
def update_note(request, slug):
    if request.method == "POST":
        post = get_object_or_404(Note, pk=slug)
        note = Note.objects.get(pk=slug)
        if post.has_key('title'):
            note.title = post['title']
        if post.has_key('text'):
            note.text = post['text']
        note.save()
        return HttpResponseRedirect(note.get_absolute_url())
    error_msg = u"No POST data sent."
    return HttpResponseServerError(error_msg)
