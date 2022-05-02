from django.shortcuts import render
from person.models import Person

def list_person(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'index.html', context)


