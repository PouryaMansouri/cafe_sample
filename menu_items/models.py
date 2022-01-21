from django.db import models

# Create your models here.
from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=250, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent', verbose_name='Parent Category')
    ...

