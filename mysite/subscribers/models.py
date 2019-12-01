from django.db import models
from wagtail.core import blocks


# Create your models here.
class Subscribers(models.Model):
    """  A subscribers model.   """

    email = models.CharField(max_length=100, blank=False,
                             null=False, help_text="Email address")
    full_name = models.CharField(
        max_length=100, blank=False, null=False, help_text="First and last")

    def __str__(self):
        """Str repr of this object"""
        return self.full_name

    class Meta:
        verbose_name = 'Subscribers'
        verbose_name_plural = 'Subscribers dd'