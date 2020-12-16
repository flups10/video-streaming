from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Premium(models.Model):
    name = models.CharField(max_length=99)
    price = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class user_subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    premium = models.ForeignKey(Premium, on_delete=models.SET_NULL, null=True)
    subscription_type = models.CharField(default='free', max_length=30),
    date_of_last_payment = models.DateField(name=None, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_subscription(sender, instance, created, **kwargs):
    if created:
        user_subscription.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_subscription(sender, instance, **kwargs):
    instance.user_subscription.save()
