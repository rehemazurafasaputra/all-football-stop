from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

import datetime
from django.urls import reverse

from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProductForm
from main.models import Product

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.utils.html import strip_tags

import json

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def register_ajax(request):
    if request.method == 'POST':
        # Use Django's UserCreationForm to handle validation
        form = UserCreationForm(json.loads(request.body))

        if form.is_valid():
            form.save() # Create the new user
            return JsonResponse({
                "status": "success",
                "message": "Account created successfully! Please log in.",
                "redirect_url": reverse('main:login')
            }, status=200)
        else:
            return JsonResponse({
                "status": "error",
                "message": "ERROR, Please try again."
            }, status=400)
            
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def login_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": "success",
                "message": "Login successful!",
                "redirect_url": reverse('main:show_main') 
            }, status=200)
        else:
            return JsonResponse({
                "status": "error",
                "message": "Invalid username or password."
            }, status=401)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def logout_ajax(request):
    logout(request)
    redirect_url = reverse('main:login')
    return JsonResponse({
        "status": "success", 
        "message": "You have been logged out.",
        "redirect_url": redirect_url
    })

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context =  {
        'npm': "2406432072",
        'nama': "Rehema Zurafa Saputra",
        'class': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request,"main.html",context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    stock = request.POST.get("stock")
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name, 
        description=description,
        stock=stock,
        price=price,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

def edit_product(request, id):
    news = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=news)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        
        # Cek apakah product dimiliki user yang mengupdate
        if product.user != request.user:
            return JsonResponse({"status": "error", "message": "Permission denied"}, status=403)

        product.name = strip_tags(request.POST.get("name", product.name))
        product.stock = request.POST.get("stock", product.stock)
        product.price = request.POST.get("price", product.price)
        product.description = strip_tags(request.POST.get("description", product.description))
        product.category = request.POST.get("category", product.category)
        product.thumbnail = request.POST.get("thumbnail", product.thumbnail)
        product.is_featured = request.POST.get("is_featured") == 'on'
        
        product.save()
        
        return JsonResponse({"status": "success", "message": "Product updated successfully"}, status=200)
        
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product = get_object_or_404(Product, pk=id).delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)

         # Cek apakah product dimiliki user yang mendelete
        if product.user != request.user:
            return JsonResponse({"status": "error", "message": "Permission denied."}, status=403)

        product.delete()
        return JsonResponse({"status": "success", "message": "Product deleted successfully."}, status=200)

    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found."}, status=404)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

@login_required(login_url='/login')
def show_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'stock': product.stock,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_pk):
   try:
       product_item = Product.objects.get(pk=product_pk)
       xml_data = serializers.serialize("xml", [product_item])
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_pk):
    try:
        product = Product.objects.select_related('user').get(pk=product_pk)
        data = {
            'id': str(product.id),
            'name': product.name,
            'stock': product.stock,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else 'Anonymous'
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
