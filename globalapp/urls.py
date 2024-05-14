# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the 'home' view
    path('products/', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('products/add/', views.add_product, name='add_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('delete_from_cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('reviews/', views.review_list, name='review_list'),
]
    
