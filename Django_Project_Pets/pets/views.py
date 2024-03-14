from allauth.socialaccount.models import SocialAccount
from django.shortcuts import render, redirect, get_object_or_404
from django_daraja.mpesa.core import MpesaClient

from pets.forms import ClientForm
from pets.models import Product, CartItem, ClientProfile


# Create your views here.
def home(request):
    return render(request, 'my cart items/login.html')


def logout(request):
    logout(request)
    return redirect('')


def redirect_to_welcome(user):
    if SocialAccount.objects.filter(user=user, provider='google').exists():
        return redirect('welcome')  # Redirect to welcome page if authenticated via Google
    else:
        return redirect('home')  # Redirect to home page if authenticated via other means


def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'my cart items/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('pets:view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('pets:view_cart')


def payment(request, amount):
    if request.method == 'POST':
        mc = MpesaClient()
        account_reference = 'reference'
        transaction_description = 'Shopping List'
        phoneno = request.POST['phoneno']
        amount = int(request.POST['amount'])
        callback_url = 'https://api.darajambili.com/express-payment'
        mc.stk_push(phoneno, amount, account_reference, transaction_description, callback_url)
        message = f'Your payment was successfully'
        return render(request, 'my cart items/user.html', {'message': message, })
    else:
        return render(request, 'my cart items/user.html', {'amount': amount})


def client_profile(request):
    profile = ClientProfile.objects.all()
    return render(request, 'landing.html', {'profile': profile})


def client_details(request, pk):
    client_info = ClientProfile.objects.all(pk=pk)
    return render(request, 'editing/main.html', {'client_info': client_info})


def edit_profile(request, pk):
    client_info = get_object_or_404(ClientProfile, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client_info)
        if form.is_valid():
            form.save()
            return redirect('pets:client_profile')

    else:
        form = ClientForm(instance=client_info)
    return render(request, 'editing/edit.html', {'form': form})


def delete_profile(request, pk):
    client_info = get_object_or_404(ClientProfile, pk=pk)
    if request.method == 'POST':
        client_info.delete()
        return redirect('client_profile')
    return render(request, 'editing/delete.html', {'client_info': client_info})
