import datetime

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
    """
        A class used to implement tables

        ...

        Attributes
        ----------
        status : int
            the status of table, is it inuse or not
        capacity : int
            how many people can sit around this table

        Methods
        -------
        all_orders()
            :return order_query
            return all orders of this table

        Properties
        --------
        money_today(date= datetime.today())
            :return int
            date : datetime
            return sum of final price for all order for this date
        """
    status = models.IntegerField(choices=TABLE_STATUS, default=TABLE_STATUS.EMPTY)
    capacity = models.PositiveIntegerField()

    def all_orders(self):
        ...

    @property
    def money(self, date: datetime = datetime.today()) -> int:
        ...
