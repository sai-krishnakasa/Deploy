from django.shortcuts import render
from django.views import View



class home(View):
    def get(self,request):
        return render(request,'index.html')
