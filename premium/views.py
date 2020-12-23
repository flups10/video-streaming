from django.shortcuts import render
from . import models
from .forms import CheckoutForm
# Create your views here.


def premium_offers(request):

    model = models.Premium.objects.all

    context = {
        'premium': model
    }

    print(context)
    return render(request, 'premium/premium.html', context)


def checkout(request):

    form = CheckoutForm

    context = {
        'form': form,
        'stripe_public_key': 'pk_test_51HtsT9Aix7sFfA4IU61hQFnTpvq2DPliM4hCAN4chpM19M4CVk28tNiWJQ68ghGgzZypHRGz8OR186x3raBFRcJs00CVE4VVqH',
        'client_secret': 'test_secret' 
    }

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'country': request.POST['country']
        }

    return render(request, 'premium/checkout.html', context)
