#django
from django.shortcuts import render, redirect
from django.contrib import messages

#self made
from .forms import DistrictForm, StreetForm, LocalsForm, LocalProductsForm, LocalStaff
from .models import District, Street, Locals, LocalProducts, LocalStaff

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
    context = {'form':form, 'district':district}
    return render(request, 'places/forms/district_form.html', context)


def street_list(request):                                                      #try to make street add/rename without this function
    streets = Street.objects.all()
    context = {'streets':streets}
    return render(request, 'places/forms/street_list.html', context)

def street(request, pk):
    street = Street.objects.get(id=pk)
    form = StreetForm()
    if request.method == "POST":
        new_name = request.POST.get('name')
        street.name = new_name
        street.save()
        return redirect('/miejsca/street_list')
    context = {'form':form, 'street':street}
    return render(request, 'places/forms/street_form.html', context)


def local_list(request):
    locals = Locals.objects.all()
    context = {'locals':locals}
    return render(request, 'places/forms/locals_list.html', context)

def local_form(request, pk):
    local = Locals.objects.get(id=pk)
    form = LocalsForm()
    if request.method == "POST":
        print(request.POST.get('name'), 'name')
        if request.POST.get('name') != "":
            local.name = request.POST.get('name')
        else:
            local.name = local.name
        if request.POST.get('description') != "":
            local.description = request.POST.get('description')
        else:
            local.description = local.description
        local.save()
        return redirect('local_list')            
    context = {'local':local, 'form':form}
    return render(request, 'places/forms/local_form.html', context)

def local_add(request):
    form = LocalsForm()
    context = {'form':form}
    if request.method == 'POST':
        name_request = request.POST.get('name')
        description_request = request.POST.get('description')
        local_street_request = request.POST.get('local_street')
        local_addres_request = request.POST.get('local_addres')
        if name_request == '' or local_street_request == '' or local_addres_request == '':
            messages.info(request, 'Aby klienci wiedzieli o tym miejscu musisz podać adres, ulice, nazwę.')
            return redirect('local_add')
        else:
            Locals.objects.create(
                name = name_request, 
                description = description_request,
                local_street = Street.objects.get(id=local_street_request),
                local_addres = local_addres_request
            )
            return redirect('local_list')
    return render(request, 'places/forms/local_add.html', context)

def local_delete(request, pk):
    local_request = Locals.objects.get(id=pk)
    if request.method == "POST":
        local_request.delete()
        return redirect('local_list')
    return render(request, 'places/forms/local_delete.html', {'local_request':local_request})