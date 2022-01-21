from django.db import models
from model_utils import Choices

# Create your models here.
from core.models import BaseModel

ITEM_STATUS = Choices(
    (0, 'AVAILABLE', 'Available for menu'),
    (1, 'UNAVAILABLE', 'Unavailable for Menu'),
)


class Category(BaseModel):
    name = models.CharField(verbose_name='Name', max_length=250, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent', verbose_name='Parent Category',
                               null=True, blank=True)
    ...


class MenuItem(BaseModel):
    name = models.CharField(max_length=250, unique=True, verbose_name='Item name')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    status = models.IntegerField(choices=ITEM_STATUS, default=ITEM_STATUS.AVAILABLE)
    price = models.PositiveIntegerField(verbose_name='Price')
    discount = models.PositiveIntegerField(verbose_name='Discount')
    ...
