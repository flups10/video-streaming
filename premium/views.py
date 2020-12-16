from django.shortcuts import render
from . import models
# Create your views here.


def premium_offers(request):

    model = models.Premium.objects.all

    context = {
        'premium': model
    }

    print(context)
    return render(request, 'premium/premium.html', context)


def checkout(request):
    print(models.user_subscription.user)
    return render(request, 'premium/checkout.html')
