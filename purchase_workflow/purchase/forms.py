from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PurchaseOrder, Vendor, Product

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','password1','email')

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['vendor_id','order_date','delivery_date']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__" 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'style': 'resize:none;width:200px;height:100px;',  # this will disallow resizing the textarea
        }),
        required=False
    )

    reserved_quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '0'}),
        required=False
    )

    available_quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '0'}),
        required=False
    )

    length = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '0'}),
        required=False
    )


    width = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '0'}),
        required=False
    )

    height = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '0'}),
        required=False
    )

    weight = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '0'}),
        required=False
    )

    volume = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '0'}),
        required=False
    )

    supplier_ids = forms.ModelMultipleChoiceField(
        queryset=Vendor.objects.all(),
        required=False
    )
