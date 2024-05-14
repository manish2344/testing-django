# views.py
from django.shortcuts import render, redirect
from .models import Product, OrderItem, Order
from .forms import ProductForm
from .models import Category, Review
def home(request):
    return render(request, 'home.html')


from django.shortcuts import redirect

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to product list page after saving
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Check if there is an active order for the current user
    order, created = Order.objects.get_or_create(user=request.user, total_amount=0)
    
    # Create the order item associated with the order
    OrderItem.objects.create(order=order, product=product, quantity=1, price=product.price)
    
    return redirect('view_cart') 

def view_cart(request):
    cart_items = OrderItem.objects.all()
    return render(request, 'view_cart.html', {'cart_items': cart_items})

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def delete_from_cart(request, item_id):
    order_item = OrderItem.objects.get(id=item_id)
    order_item.delete()
    return redirect('view_cart')


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})
