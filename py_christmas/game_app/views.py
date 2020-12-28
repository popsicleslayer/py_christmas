from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from game_app.models import Place, Way

# Create your views here.
class MainPage(View):
    """
    Main page view
    """
    #
    def get(self, request):
        try:
            current_place_id = request.session['current_place']
        except:
            place_id = Place.objects.order_by('pk').first()
            request.session['current_place'] = place_id.id
        current_place = Place.objects.get(pk = request.session.get('current_place'))
        outgoing_ways = current_place.outgoing_ways.all()
        context = {
            'place': current_place,
            'ways' : outgoing_ways
        }
        return render(request,'index.html', context)

class Place_view(View):
    def __str__(self):
        return Place.objects.values_list('short_description')

class Way_view(View):
    def __str__(self):
        return Way.objects.values_list('short_description')

@method_decorator(csrf_exempt, name='dispatch')
class GoToPlace_view(View):
    def post(self, request, id):
        place_id = request.session.get('current_place')
        place = Place.objects.get(pk=place_id)
        way_id = id
        for way in place.outgoing_ways.all():
            if way_id == way.pk:
                request.session['current_place'] = way.destination.pk
        return redirect('main_page')
