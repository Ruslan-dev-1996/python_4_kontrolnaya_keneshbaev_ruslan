from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.forms import PollForm
from webapp.models import Poll, Choice

class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

class PollView(DetailView):
    template_name = 'poll/detailed.html'
    model = Poll
    context_object_name = 'poll'

class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class PollUpdateView(UpdateView):
    template_name = 'poll/update.html'
    model = Poll
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class PollDeleteView(DetailView):
    model = Poll
    template_name = 'poll/delete.html'
    context_object_name = 'poll'
    error = 'error.html'

    def get_success_url(self):
        return reverse('index')