from django.shortcuts import render
from django.conf import settings
from .models import user_subscription
from django.contrib.auth import get_user_model
from .forms import CheckoutForm
import stripe
import datetime
# Create your views here.

endpoint_secret = settings.STRIPE_WH_SECRET

def premium_offers(request):

    stripe_total = settings.STRIPE_TOTAL
    context = {
        'price': stripe_total,
    }

    return render(request, 'premium/premium.html', context)


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    form = CheckoutForm
    stripe_total = settings.STRIPE_TOTAL
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
             amount=stripe_total,
             currency=settings.STRIPE_CURRENCY
         )
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    if request.method == 'POST':

        current_user_subscription = user_subscription.objects.filter(
                                    user=request.user).values('premium_until')
        if current_user_subscription:
            old_date = current_user_subscription[0]['premium_until']
            new_date = old_date + datetime.timedelta(30)
            current_user_subscription = user_subscription.objects.get(user=request.user)
            current_user_subscription.premium_until = new_date
            current_user_subscription.save()

        else:

            now = datetime.datetime.now()
            start_date = datetime.date.today() + datetime.timedelta(30)
            dict = {
                'user': request.user,
                'premium_until': start_date,
                'date_of_last_payment': now
            }

            user_subscription.objects.create(**dict)


    return render(request, 'premium/checkout.html', context)
