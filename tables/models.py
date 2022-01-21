from django.db import models

# Create your models here.
from core.models import BaseModel
from model_utils import Choices

TABLE_STATUS = Choices(
    (0, 'EMPTY', 'Empty'),
    (1, 'FULL', 'Full'),
    (2, 'RESERVED', 'Reserved')
)


class Table(BaseModel):
    status = models.IntegerField(choices=TABLE_STATUS, default=TABLE_STATUS.EMPTY)
    capacity = models.PositiveIntegerField()

    @property
    def all_orders(self):
        ...
