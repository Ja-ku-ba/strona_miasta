#django
from django.shortcuts import render, redirect

#self made
from .forms import DistrictForm
from .models import District

# Create your views here.
def places_forms(request):
    return render(request, 'places/places_forms.html')

def district_list(request):                                                    #try to make district add/rename without this function
    districts = District.objects.all()
    context = {'districts':districts}
    return render(request, 'places/forms/districts_list.html', context)

def district(request, pk):
    district = District.objects.get(id=pk)
    form = DistrictForm()
    if request.method == "POST":
        new_name = request.POST.get('name')
        district.name = new_name
        district.save()
        return redirect('/miejsca/district_list')
    context = {'form':form}
    return render(request, 'places/forms/district_form.html', context)