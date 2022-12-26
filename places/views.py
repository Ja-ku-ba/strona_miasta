from django.shortcuts import render

# Create your views here.
def places_forms(request):
    return render(request, 'places/places_forms.html')