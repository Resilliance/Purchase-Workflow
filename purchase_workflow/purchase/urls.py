from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('vendors',views.vendors,name="vendors"),
    path('vendor_form/<int:vendor_id>/',views.vendors_form,name="vendors_form"),
    path('vendors_form_create',views.vendors_form_create,name="vendors_form_create"),
    path('products',views.products,name="products"),
    path('products_form/<int:product_id>/',views.products_form,name="products_form"),
    path('products_form_create',views.products_form_create,name="products_form_create"),
    path('users',views.users,name="users"),
    path('users_form/<int:user_id>',views.users_form,name="users_form"),
    path('users_formacreate',views.users_form_create,name="users_form_create"),

    # path('create/', views.create_po, name='create_model'),
]