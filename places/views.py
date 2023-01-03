#django
from django.shortcuts import render, redirect
from django.contrib import messages

#self made
from .forms import LocalsForm, LocalProductsForm, LocalStaff, LocalRatingForm
from .models import Locals, LocalProducts, LocalStaff, LocalRating, Street, LocalProductRating

# Create your views here.
def local_list(request):
    locals = Locals.objects.all()
    context = {'locals':locals}
    return render(request, 'places/places_card.html', context)

def local(request, pk):
    local = Locals.objects.get(id=pk)
    products = LocalProducts.objects.filter(product_local=local)
    opinions = LocalRating.objects.filter(local=local)
    context = {'local':local, 'products':products, 'opinions':opinions}
    return render(request, 'places/local.html', context)

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
                local_addres = local_addres_request,
                owner = request.user
            )
            return redirect('local_list')
    return render(request, 'places/forms/local_add.html', context)

def local_delete(request, pk):
    local_request = Locals.objects.get(id=pk)
    if request.method == "POST":
        local_request.delete()
        return redirect('local_list')
    return render(request, 'places/forms/local_delete.html', {'local_request':local_request})


def product(request, pk):
    product = LocalProducts.objects.get(id=pk)
    local = Locals.objects.get(id=product.product_local.id)
    opinions = LocalProductRating.objects.filter(product=product)

    if request.method == "POST":                                                                   #new opinion about product
        LocalProductRating.objects.create(
            opinion = request.POST.get('opinion'),
            person = request.user,
            product = product,
        )
        return redirect('product', product.id)

    context = {'product':product, 'local':local, 'opinions':opinions}
    return render(request, 'places/product.html', context)

def product_add(request, pk):
    local = Locals.objects.get(id=pk)
    if request.method == 'POST':
        new_produc = LocalProducts.objects.create(

        )
    return render(request, 'places/forms/product_add.html')

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
        return redirect('local', product.product_local.id)

def rating_list(request):
    ratings = LocalRating.objects.all()
    context = {'ratings':ratings}
    return render(request, 'places/forms/rating_list.html', context)

def rating_add(request, pk):
    local_req = Locals.objects.get(id=pk)
    if request.method == "POST":
        LocalRating.objects.create(
            opinion = request.POST.get('opinion'),
            local = local_req,
            person = request.user
        )
        return redirect('local', local_req.id)

def rating_delete(request, pk):
    try:
        rating = LocalRating.objects.get(id=pk)
        if request.method == 'POST':
            rating.delete()
            messages.info(request, 'Opinia została pomyślnie usunięta.')
            return redirect('local', rating.local.id)
    except:
        rating = LocalProductRating.objects.get(id=pk)
        if request.method == 'POST':
            rating.delete()
            messages.info(request, 'Opinia została pomyślnie usunięta.')
            return redirect('product', rating.product.id)