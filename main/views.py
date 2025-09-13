from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    product_list = Product.objects.all()

    context =  {
        'npm': "2406432072",
        'nama': "Rehema Zurafa Saputra",
        'product_list': product_list
    }
    return render(request,"main.html",context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

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
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_pk):
   try:
       product_item = Product.objects.get(pk=product_pk)
       xml_data = serializers.serialize("xml", [product_item])
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_pk):
   try:
       product_item = Product.objects.get(pk=product_pk)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
