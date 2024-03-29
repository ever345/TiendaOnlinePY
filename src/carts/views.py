
from django.shortcuts import render,redirect,get_object_or_404
from carts.utils import get_or_create_cart
from carts.models import Cart
from products.models import Products 
from carts.models import CartProducts

def cart(request):
    cart = get_or_create_cart(request)
    return render(request, 'carts/carts.html', {'cart':cart})

def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Products,pk=request.POST.get('product_id'))
    #product = Products.objects.get(pk=request.POST.get('product_id'))
    print('vdfvsdnjvnskjhhvjhbdf',product)
    quantify = int(request.POST.get('quantify', 1))
    cart_product = CartProducts.objects.create_or_update_quantify(
        cart=cart,
        product=product,
        quantify=quantify,
    )
    
    return render(request, 'carts/add.html',{
        'quantify':quantify,
        'cart_product':cart_product,
        'product':product,
    })
    
def remove(request):
    cart = get_or_create_cart(request)
    prod = get_object_or_404(Products,pk=request.POST.get('product_id'))
    product = Products.objects.get(pk=request.POST.get('product_id'))
    
    cart.products.remove(product)
    return redirect('carts:cart')