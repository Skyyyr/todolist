from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from todo_app.models import TodoTask


def home(request):
    tasks = {
        'tasks': TodoTask.objects.all()
    }
    return render(request, 'todo_app/home.html', tasks)


class TodoCreateView(CreateView):
    model = TodoTask
    fields = ['title', 'details']


class TodoDetailView(DetailView):
    model = TodoTask


class TodoUpdateView(UpdateView):
    model = TodoTask
    fields = ['title', 'details']


class TodoDeleteView(DeleteView):
    model = TodoTask
    success_url = '/'
