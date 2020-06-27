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

def token(request):
    result ='''<pre>
    
    d475ef8e15a302fb22103ea21df6d06f0557d995
    append /token-auth/ and you can use this token authentication for apis
    <a href="/token-auth/">Click to Invalidated</a>
    <a href="/token-auth/%20username=admin%20password=admin">Click to Validate</a>
    
    <a href="/token-auth/show/">Click to access token based api</a>
    </pre>'''
    return HttpResponse(result)
