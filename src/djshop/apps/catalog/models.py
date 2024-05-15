from django.db import models
from treebeard.mp_tree import MP_Node


# Create your models here.


class test(models.Model):
    title = models.CharField(
        max_length=255
    )


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=2048, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(
        default='',
        null=False,
        db_index=True,
        verbose_name='Slug',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'Website_Category'  # & table name in database
        db_tablespace = 'logs'
        ordering = ['-title']
        unique_together = [
            ['title', 'description', 'slug']
        ]
        # abstract = True
        # proxy = True


class LogField(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(LogField):
    title = models.CharField(max_length=255)
    price = models.IntegerField()


class DigitalProduct(Product):
    cpu = models.CharField(max_length=255)



