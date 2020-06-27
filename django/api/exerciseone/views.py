import random

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse

from .forms import RouterForm
from .models import Router


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('exerciseone/index.html')
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def generatedata(request):
    for x in range(5):
        router = Router.objects.create(sapid=x,hostname="hostname",loopback="loopback",macaddress="121312")
        router.save()
    return redirect(index)

def router(request):
    if request.method == "POST":
        form = RouterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            try:
                form.save()
                return redirect(show)
            except Exception as e:
                print(e)
    else:
        form = RouterForm()
    return render(request,'exerciseone/create.html',{'form':form})

def show(request):
    router = Router.objects.filter(is_deleted=0)
    print(router)
    return render(request,"exerciseone/show.html",{'router':router})

def edit(request, id):
    router = Router.objects.get(id=id)
    return render(request,'exerciseone/edit.html', {'router':router})


def update(request, id):
    router = Router.objects.get(id=id)
    form = RouterForm(request.POST, instance = router)
    if form.is_valid():
        form.save()
        return redirect(show)
    return render(request, 'exerciseone/edit.html', {'router': router})


def destroy(request, id):
    router = Router.objects.get(id=id)
    router.is_deleted = 1
    router.save()
    return redirect(show)

def deleteonip(request, id):
    router = Router.objects.filter(loopback=id)
    router.update(is_deleted=1)
    return redirect(show)