from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request,
                  'products.html',
                  {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

