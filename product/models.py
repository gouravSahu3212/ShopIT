import os

from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to=os.path.join(settings.STATIC_ROOT, 'products'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the product, which is the product's title.
        """
        return self.title

    def save(self, *args, **kwargs) -> None:
        """
        Overrides the default save() method to automatically generate a slug from the title if one is not provided.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
