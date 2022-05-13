from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from .models import Friend

"""
class HelloView(TemplateView):
    def __init__(self):
        self.params={
            'title':'Hello',
            'message':'your data',
            'form':HelloForm(),
            }
    def get(self,request):
        return render(request,'hello/index.html',self.params)
    
    def post(self,request):
        msg='あなたは,<b>'+request.POST['name']+\
            '(' +request.POST['age']+ ')</b>さんですね。<br>メアドは<b>' \
            +request.POST['mail']+'ですね。'\
            '<br>身長は'+request.POST['height']+'でしたね。'
        self.params['message']=msg
        self.params['form']=HelloForm(request.POST)
        return render(request,'hello/index.html',self.params)
"""

def index(request):
    data=Friend.objects.all()
    params={
        'title':'Hello',
        'message':'all friends',
        'data':data,
    }
    return render(request,'hello/index.html',params)