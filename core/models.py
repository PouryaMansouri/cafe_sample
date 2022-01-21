from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.manager import BaseManager


class BaseModel(models.Model):
    """
        This model mixin usable for logical delete and logical activate status datas.
    """
    created = models.DateTimeField(auto_now_add=True, editable=False, )
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    delete_timestamp = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(
        null=True, blank=True,
        verbose_name=_("Deleted Datetime"),
        help_text=_("This is deleted datetime")
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_("Deleted status"),
        help_text=_("This is deleted status")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active status"),
        help_text=_("This is active status")
    )

    # custom manager for get active items
    objects = BaseManager()

    class Meta:
        abstract = True

    def deleter(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()
