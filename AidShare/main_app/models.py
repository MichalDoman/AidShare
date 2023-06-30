from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)


class Institution(models.Model):
    INSTITUTION_TYPES = [
        ("foundation", "Foundation"),
        ("non-governmental organization", "Non-governmental organization"),
        ("local collection", "Local collection"),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=INSTITUTION_TYPES, default="foundation")
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
