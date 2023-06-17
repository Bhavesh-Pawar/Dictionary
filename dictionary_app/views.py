import requests

from django.shortcuts import render , redirect
from django.views import View 
from django.views.generic import TemplateView
from django.http.response import JsonResponse
from django.conf import settings

# Create your views here.

class HomeView(View):
    template_name = "home.html"

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        action = request.POST.get('action','')
        if action:
            word = request.POST.get('word','')
            response = requests.get(f'{settings.DICT_API}{word}')
            print(response.text)
            return JsonResponse({'data':response.json()})
        else:
            return redirect('home')

