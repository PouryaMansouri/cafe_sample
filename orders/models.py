from django.db import models

# Create your models here.
from model_utils import Choices

from core.models import BaseModel
from menu_items.models import MenuItem

ORDER_STATUS = Choices(
    (0, 'CANCEL', 'Cancel'),
    (1, 'UNPAID', 'Unpaid'),
    (2, 'PAIN', 'Paid')
)


class Order(BaseModel):
    status = models.IntegerField(choices=ORDER_STATUS, default=ORDER_STATUS.UNPAID, verbose_name='Status')
    is_paid = models.BooleanField(default=False, verbose_name='Paid')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id} status :{self.status} '

    @property
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE, verbose_name='Order')
    item = models.ForeignKey(MenuItem, related_name='menu_items', on_delete=models.CASCADE,
                             verbose_name='Item')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')

    def __str__(self):
        return f"{self.quantity} * {self.item.name}"

    @property
    def get_cost(self):
        return (self.item.price - self.item.discount) * self.quantity
