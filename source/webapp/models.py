from django.db import models

class Poll(models.Model):
    questions = models.TextField(max_length=200, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.questions
class Choice(models.Model):
    text = models.TextField(max_length=100, null=False, blank=False, verbose_name='Текст')
    poll = models.ForeignKey('webapp.Poll', related_name='polls',
                                on_delete=models.PROTECT, verbose_name='опрос')

class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll',  null=False, blank=False, related_name='pollss', on_delete=models.PROTECT, verbose_name='опрос')
    choice = models.ForeignKey('webapp.Choice',  null=False, blank=False, related_name='choices', on_delete=models.PROTECT, verbose_name='выбор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
