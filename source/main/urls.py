"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, PollView, PollCreateView, PollUpdateView, PollDeleteView,\
ChoiceView,  ChoiceDetailView, ChoiceCreateView, ChoiceUpdateView, ChoiceDeleteView, AnswerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>', PollView.as_view(), name='poll_view'),
    path('poll/add/', PollCreateView.as_view(), name='poll_add'),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
    path('choice/view', ChoiceView.as_view(), name='choice_view'),
    path('choice/<int:pk>/detail',  ChoiceDetailView.as_view(), name='detail_view'),
    path('choice/add/', ChoiceCreateView.as_view(), name='choice_add'),
    path('choice/<int:pk>/update/', ChoiceUpdateView.as_view(), name='choice_update'),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name='choice_delete'),
    path('answer/view', AnswerView.as_view(), name='answer_view')

]
