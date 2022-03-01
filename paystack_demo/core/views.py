from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import forms


# Create your views here.
def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            render(request, 'make_payment.html', {'payment_form': payment})
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'initiate_payment.html', {'payment_form': payment_form})


