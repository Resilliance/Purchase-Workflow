from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import PurchaseOrderForm, VendorForm, ProductForm
from .models import PurchaseOrder, Vendor, Product


# Create your views here.
def home(request):
    values = {}
    values['pos'] = PurchaseOrder.objects.all()
    values['path'] = request.path
    return render(request, 'home.html',{'values':values})

def vendors(request):
    values = {}
    values['vendors'] = Vendor.objects.all()
    values['path'] = request.path
    return render(request, 'vendors.html',{'values':values})

def vendors_form(request, vendor_id):
    model_instance = get_object_or_404(Vendor, pk=vendor_id)

    if request.method == 'POST':
        values = VendorForm(request.POST, instance=model_instance)
        if values.is_valid():
            values.save()
            return redirect('vendors_form',vendor_id=vendor_id)
    else:
        values = VendorForm(instance=model_instance)
    return render(request, 'vendors_form.html',{'values':values})

def vendors_form_create(request):
    if request.method == 'POST':
        values = VendorForm(request.POST)
        if values.is_valid():
            vendor = values.save()
            return redirect('vendors_form',vendor_id=vendor.id)
    else:
        values = VendorForm()
    return render(request, 'vendors_form_create.html',{'values':values})
    

def products(request):
    values = {}
    values['products'] = Product.objects.all()
    paginator = Paginator(values['products'],10)

    page = request.GET.get('page')
    try:
        values['pages'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        values['pages'] = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        values['pages'] = paginator.page(paginator.num_pages)

    values['path'] = request.path
    return render(request, 'products.html',{'values':values})

def products_form(request,product_id):
    model_instance = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        values = ProductForm(request.POST, instance=model_instance)
        if values.is_valid():
            values.save()
            return redirect('products_form',product_id=product_id)
    else:
        # print(values)
        values = ProductForm(instance=model_instance)
    return render(request, 'products_form.html',{'values':values})

def products_form_create(request):
    if request.method == 'POST':
        values = ProductForm(request.POST)
        if values.is_valid():
            product = values.save()
            return redirect('products_form',product_id=product.id)
    else:
        values = ProductForm()
    return render(request, 'products_form_create.html',{'values':values})

def users(request):
    values = {}
    values['users'] = User.objects.all()
    values['path'] = request.path
    return render(request,'users.html',{'values':values})

def users_form(request,user_id):
    model_instance = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        values = UserCreationForm(request.POST, instance=model_instance)
        if values.is_valid():
            values.save()
            return redirect('users_form',user_id=user_id)
    else:
        values = UserCreationForm(instance=model_instance)
    return render(request, 'users_form.html',{'values':values})


def users_form_create(request):
    if request.method == 'POST':
        values = UserCreationForm(request.POST)
        if values.is_valid():
            user = values.save()
            return redirect('users_form',user_id=user.id)
    else:
        values = UserCreationForm()
    return render(request, 'users_form_create.html', {'values': values})
