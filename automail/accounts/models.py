from django.db import models


CITY_CHOICES = (
    ('Mumbai', 'Mumbai'),
    ('Delhi', 'Delhi'),
    ('Chennai', 'Chennai'),
    ('Banglore', 'Banglore'),
    ('Kolkata', 'Kolkata'),
)


class Receiver(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=250, choices=CITY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Receivers'
        verbose_name_plural = 'Receivers'

    def __str__(self):
        return self.full_name

