from django.urls import reverse
from webapp.forms import ChoiceForm
from webapp.models import Choice
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


class ChoiceView(ListView):
    template_name = 'choice/choice_view.html'
    model = Choice
    context_object_name = 'choices'



class ChoiceDetailView(DetailView):
    template_name = 'choice/detail_choice.html'
    model = Choice
    context_object_name = 'choice'


class ChoiceCreateView(CreateView):
    template_name = 'choice/create_choice.html'
    model = Choice
    form_class = ChoiceForm
    def get_success_url(self):
        return reverse('choice_view')

class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update_choice.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('choice_view')



class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/delete_choice.html'
    context_object_name = 'choice'
    # error = 'error.html'

    def get_success_url(self):
        return reverse('choice_view')