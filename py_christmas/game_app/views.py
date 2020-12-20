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

class Place(View):
    def __str__(self):
        return Place.objects.values_list('short_description')