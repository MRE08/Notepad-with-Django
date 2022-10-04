from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Notes
from django.template import RequestContext
# Create your views here.

def home(request):
    notes = Notes.objects.all().values
    context = {
        'notes':notes
    }
    return render(request, 'home/home.html', context)

def create(request):

    return render(request, 'home/create.html')

def createnote(request):
    x = request.POST['newtitle']
    y = request.POST['newdescription']
    notes = Notes(title=x, description=y)
    notes.save()
    return HttpResponseRedirect(reverse('home'))

def update(request,id):
    note= Notes.objects.get(id=id)
    context = {
        'note':note
    }
    return render(request, 'home/update.html', context)

def updaterecord(request,id):
    title = request.POST['newtitle']
    description = request.POST['newdescription']
    note = Notes.objects.get(id=id)
    note.title = title
    note.description = description
    note.save()
    return HttpResponseRedirect (reverse('home'))

def deleterecord(request,id):
    notes = Notes.objects.get(id=id)
    notes.delete()
    return HttpResponseRedirect (reverse('home'))