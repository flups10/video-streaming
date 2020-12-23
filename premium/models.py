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
    date_of_last_payment = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_subscription(sender, instance, created, **kwargs):
    if created:
        user_subscription.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_subscription(sender, instance, **kwargs):
    instance.user_subscription.save()


class checkout(models.Model):

    subscription_number = models.CharField(max_length=32,
                                           null=False, editable=False)
    full_name = models.CharField(max_length=69, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = models.CharField(max_length=69, null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=False,
                                blank=True)


    """
    this code was taken from ckz8780
    """
    def _generate_subscription_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.subscription_number:
            self.subscription_number = self._generate_subscription_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subscription_number
