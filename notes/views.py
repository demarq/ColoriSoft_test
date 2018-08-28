from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Notes
from .forms import AddNoteForm


def home(request):
    context = {}
    if request.method == 'GET':
        context.update({'notes': Notes.objects.order_by('-unique_symbols'),
                        'form': AddNoteForm})

    elif request.method == 'POST':
        form = AddNoteForm(request.POST)
        context.update({'form': form})
        if form.is_valid():
            is_success = form.save()
            if not is_success:
                render(request, 'notes/woops.html', {})
            return HttpResponseRedirect(reverse('notes'))

    return render(request, 'notes/notes.html', context)