from django.db import models

# Create your models here.
from model_utils import Choices

from core.models import BaseModel

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

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
