from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskCreateForm
from django.urls import reverse_lazy




class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('task:task-list')


class TaskDetailView(DetailView):
    model = Task
    fields = ['title', 'completed']
    success_url = reverse_lazy('task:task-list')
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('task:task-list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task:task-list')
