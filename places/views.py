#python
import os

#django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#self made
from .forms import LocalsForm, LocalProductsForm
from .models import Locals, LocalProducts, LocalRating, Street, LocalProductRating, District, PlaceFavourite, PlaceToVisit

# Create your views here.
def local_list(request):
    locals1 = Locals.objects.order_by("?")
    locals2 = Locals.objects.order_by("?")
    locals3 = Locals.objects.order_by("?")
    locals4 = Locals.objects.order_by("?")
    locals5 = Locals.objects.order_by("?")
    context = {'locals1':locals1, 'locals2':locals2, 'locals3':locals3, 'locals4':locals4, 'locals5':locals5}
    return render(request, 'places/places_card.html', context)

def local(request, pk):
    local = Locals.objects.get(id=pk)
    products = LocalProducts.objects.filter(product_local=local).order_by('name')
    opinions = LocalRating.objects.filter(local=local)
    try:
        fav_status = PlaceFavourite.objects.get(local=local, user=request.user)
    except:
        fav_status = ''
    try:
        vis_status = PlaceToVisit.objects.get(local=local, user=request.user)
    except:
        vis_status = ""
    context = {'local':local, 'products':products, 'opinions':opinions, 'fav_status':fav_status, 'vis_status':vis_status}
    return render(request, 'places/local.html', context)

def remove_img(path, img_name):
    if os.path.exists(path + '/' + img_name) is False:
        # file did not exists
        return False
    os.remove(path + '/' + img_name)
    return True

@login_required
def local_edit(request, pk):
    local = Locals.objects.get(id=pk)
    streets = Street.objects.all()
    if request.method == "POST":
        if request.POST.get('name') != "":
            local.name = request.POST.get('name')
        if request.POST.get('description') != "":
            local.description = request.POST.get('description')
        if request.POST.get('local_street') != "":
            street_req = request.POST.get('local_street')
            street = Street.objects.get(street_req)
            local.local_street = street
        if request.POST.get('local_addres') != "":
            local.local_addres = request.POST.get('local_addres')
        if request.FILES.get('logo') is not None:
            try:
                local.logo.delete()
            except:
                pass
            remove_img(f"C:/Users/jakub/Desktop/strona_miasta/places/static/locals/{local.id}", 'logo.png')
            local.logo = request.FILES.get('logo')
            local.save()
        return redirect('local_list')            
    context = {'local':local, 'streets':streets}
    return render(request, 'places/forms/local_form.html', context)

@login_required
def local_add(request):
    form = LocalsForm(request.POST, request.FILES)
    streets = Street.objects.all()
    context = {'form':form, 'streets':streets}
    if request.method == 'POST':
        name_request = request.POST.get('name')
        description_request = request.POST.get('description')
        local_street_request = request.POST.get('local_street')
        local_addres_request = request.POST.get('local_addres')
        if name_request == '' or local_street_request == '' or local_addres_request == '':
            messages.info(request, 'Aby klienci wiedzieli o tym miejscu musisz podać adres, ulice, nazwę.')
            return redirect('local_add')
        else:
            new_local = Locals.objects.create(
                name = name_request, 
                description = description_request,
                local_street = Street.objects.get(name=local_street_request),
                local_addres = local_addres_request,
                owner = request.user
            )
            new_local.logo = request.FILES.get('logo')
            new_local.save()
            return redirect('local_list')
    return render(request, 'places/forms/local_add.html', context)

@login_required
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

@login_required
def product_add(request, pk):
    local = Locals.objects.get(id=pk)
    form = LocalProductsForm(request.POST, request.FILES)
    if request.method == 'POST':
        new_product = LocalProducts.objects.create(
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            price = request.POST.get('price'),
            product_local = local
        )
        new_product.product_image = request.FILES.get('product_image')
        new_product.save()
        return redirect('local', local.id)
    context = {'form':form}
    return render(request, 'places/forms/product_add.html', context)

@login_required
def product_edit(request, pk):
    product = LocalProducts.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST.get('name') != "":
            product.name = request.POST.get('name')
        if request.POST.get('description') != "":
            product.description = request.POST.get('description')
        if request.POST.get('price') != "":
            product.description = request.POST.get('price')
        if request.FILES.get('product_image') is not None:
            try:
                product.product_image.delete()                                                       #if ther is no product photo
            except:
                pass
            remove_img(f"C:/Users/jakub/Desktop/strona_miasta/places/static/locals/{product.product_local.id}/products/", f'{product.id}.png')
            product.product_image = request.FILES.get('product_image')
            product.save()
        return redirect('product', product.id)
    context = {'product':product}
    return render(request, 'places/forms/product_edit.html', context)

@login_required
def product_delete(request, pk):
    product = LocalProducts.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('local', product.product_local.id)

def rating_list(request):
    opinions = LocalRating.objects.filter(person=request.user)
    context = {'opinions':opinions}
    return render(request, 'places/opinions.html', context)

@login_required
def rating_add(request, pk):
    local_req = Locals.objects.get(id=pk)
    if request.method == "POST":
        LocalRating.objects.create(
            opinion = request.POST.get('opinion'),
            local = local_req,
            person = request.user
        )
        return redirect('local', local_req.id)

@login_required
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


def place_locals(request, name, pk):
    dstcst = ["Środkowa", "Zewnętrzna", "Wewnętrzna", "Wyspa"]
    status = ''
    if name in dstcst:
        area = District.objects.get(id=pk)
        places = area.street_set.order_by("?")
        status = 'dis'
        context = {'status':status, 'places':places}
    else:
        area = Street.objects.get(id=pk)
        places1 = area.locals_set.order_by("?")
        places2 = area.locals_set.order_by("?")
        places3 = area.locals_set.order_by("?")
        places4 = area.locals_set.order_by("?")
        places5 = area.locals_set.order_by("?")
        context = {'places1':places1, 'places2':places2, 'places3':places3, 'places4':places4, 'places5':places5, 'status':status, 'area':area}
    return render(request, 'places/place_locals.html', context)

@login_required
def user_visit(request):
    places = Locals.objects.all()
    locals = PlaceToVisit.objects.filter(user=request.user).order_by("?")
    context = {'locals':locals, 'places':places}
    return render(request, 'places/visit_favourite.html', context)

@login_required
def user_favourite(request):
    places = Locals.objects.all()
    locals = PlaceFavourite.objects.filter(user=request.user)
    context = {'locals':locals ,'places':places}
    return render(request, 'places/visit_favourite.html', context)

@login_required
def user_vis_fav_form(request, pk):
    local = Locals.objects.get(id=pk)
    if request.method == 'POST':
        fav = request.POST.get('fav')
        vis = request.POST.get('vis')
        try:
            fav_status = PlaceFavourite.objects.get(local=local, user=request.user)
        except:
            fav_status = None
        try:
            vis_status = PlaceToVisit.objects.get(local=local, user=request.user)
        except:
            vis_status = None
            
        if fav == 'on':
            PlaceFavourite.objects.create(
                local = local,
                user = request.user,
                user_like = True
            )
        if fav == 'fav-off':
            fav_status.delete()

        if vis == 'on':
            PlaceToVisit.objects.create(
                local = local,
                user = request.user,
                want_to_visit = True
            )
        if  vis == "vis-off":
            vis_status.delete()
            
        return redirect("local", local.id)