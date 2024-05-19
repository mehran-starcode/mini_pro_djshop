from django.db import models
from treebeard.mp_tree import MP_Node
# Create your models here.


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    in_public = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

