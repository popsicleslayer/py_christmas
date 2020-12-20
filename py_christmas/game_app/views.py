from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator

# Create your views here.
class MainPage(View):
    """
    Main page view
    """
    #
    def get(self, request):
        return render(request,'index.html')