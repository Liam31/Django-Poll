from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.template import loader

from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

class PollDetailView(DetailView):
    model = Question

    template_name = "polls/polldetail.html"

    def get_context_data(self, **kwargs):
        # Where data is manipulated before sent to front
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

