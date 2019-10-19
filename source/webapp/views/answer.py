from django.views.generic import ListView
from webapp.models import Answer, Poll


class AnswerView(ListView):

    template_name = 'answer/answer.html'
    context_object_name = 'answers'
    model = Answer
    paginate_by = 5
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['polls'] = Poll.objects.all()
        return context