from apps.tasks.forms import TaskForm
from apps.tasks.models import Task
from apps.tasks.mixins import UserIsOwnerMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(UserIsOwnerMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Task created successfully.')
        return response


class TaskUpdateView(UserIsOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Task updated successfully.')
        return response


class TaskDeleteView(UserIsOwnerMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Task deleted successfully.')
        return response
    
