from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from exerciseone.models import Router
from exerciseone.views import show

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('exercisethree/index.html')
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def destroyonip(request):
    return redirect(show)