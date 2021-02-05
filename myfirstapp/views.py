from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse

def index(request):
    Content = request.GET
    request.session['AllInput'] = Content
    if Content.get('submit') == "Clicked":
        return redirect('KIT/')
    return render(request, 'home.html',{'':'batch8A'})

def KITPAGE(request):
    Input = request.session['AllInput']
    print(Input)
    return render(request, 'KIT.html',{'name': Input.get('name'),'RegNo': Input.get('reg'),'DepNo': Input.get('dep')})


