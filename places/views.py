#django
from django.shortcuts import render, redirect
from django.contrib import messages

#self made
from .forms import LocalsForm, LocalProductsForm, LocalStaff, LocalRatingForm
from .models import Locals, LocalProducts, LocalStaff, LocalRating, Street

# Create your views here.
def local_list(request):
    locals = Locals.objects.all()
    context = {'locals':locals}
    return render(request, 'core/places_card.html', context)

def local_form(request, pk):                                                   #local edit
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
    streets = Street.objects.all()
    context = {'form':form, 'streets':streets}
    if request.method == 'POST':
        name_request = request.POST.get('name')
        description_request = request.POST.get('description')
        local_street_request = request.POST.get('local_street')
        local_addres_request = request.POST.get('local_addres')
        if name_request == '' or local_street_request == '' or local_addres_request == '':
            messages.info(request, 'Aby klienci wiedzieli o tym miejscu musisz podać adres, ulice, nazwę.')
            return redirect('home')
        else:
            Locals.objects.create(
                name = name_request, 
                description = description_request,
                local_street = Street.objects.get(name=local_street_request),
                local_addres = local_addres_request
            )
            return redirect('home')
    return render(request, 'places/forms/local_add.html', context)

def local_delete(request, pk):
    local_request = Locals.objects.get(id=pk)
    if request.method == "POST":
        local_request.delete()
        return redirect('local_list')
    return render(request, 'places/forms/local_delete.html', {'local_request':local_request})


def product_list(request):
    products = LocalProducts.objects.all()
    context = {'products':products}
    return render(request, 'places/forms/product_list.html', context)

def product_add(request):
    form = LocalProductsForm()
    context = {'form':form}
    if request.method == 'POST':
        form = LocalProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'places/forms/product_add.html', context)

def product_edit(request, pk):
    product = LocalProducts.objects.get(id=pk)
    context = {'product':product}
    if request.method == 'POST':
        if request.POST.get('name') != "":
            product.name = request.POST.get('name')
        if request.POST.get('description') != "":
            product.description = request.POST.get('description')
        if request.POST.get('price') != "":
            product.description = request.POST.get('price')
        product.save()
        return redirect('product_list')
    return render(request, 'places/forms/product_edit.html', context)

def product_delete(request, pk):
    product = LocalProducts.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'places/forms/product_delete.html')


def rating_list(request):
    ratings = LocalRating.objects.all()
    context = {'ratings':ratings}
    return render(request, 'places/forms/rating_list.html', context)

def rating_add(request):
    form = LocalRatingForm()
    context = {'form':form}
    if request.method == "POST":
        form = LocalRatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rating_list')
    return render(request, 'places/forms/rating_add.html', context)

def rating_edit(request, pk):
    rating = LocalRating.objects.get(id=pk)
    context = {'rating':rating}
    if request.method == 'POST':
        if request.POST.get('opinion') != "":
            rating.opinion = request.POST.get('opinion')
        if request.POST.get('rating') != "":
            rating.rating = request.POST.get('rating')
        rating.save()
        return redirect('rating_list')
    return render(request, 'places/forms/rating_edit.html', context)

def rating_delete(request, pk):
    rating = LocalRating.objects.get(id=pk)
    context = {'rating':rating}
    if request.method == 'POST':
        rating.delete()
        return redirect('rating_list')
    return render(request, 'places/forms/rating_delete.html', context)