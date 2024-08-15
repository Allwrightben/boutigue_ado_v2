from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PkqkrP7lJBmhisM5ZN4I77HOoH7mkMzR9XpP7jHBKBTn3q87fisYhJgEEozEo3FZyRh0vKZiJ6nA09IaIVPf4q100M6rdXcqd',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)