from django import  forms
from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []

class ChoiceForm(forms.ModelForm):
    class Meta:
        model =Choice
        exclude = []


class AnswerForm(forms.ModelForm):
    class Meta:
        model =Answer
        exclude = []
