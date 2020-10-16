from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class MainView(View):
    def get(self, request):
        return render(request, 'main/landing_page.html')

class MenuListView(View):
    def get(self, request):
        return render(request, 'main/main_page.html')