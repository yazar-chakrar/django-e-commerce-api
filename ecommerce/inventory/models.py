from tabnanny import verbose

from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


# Create your models here.
class Category(MPTTModel):
    """
    Inventory category table implimented with MPTT
    """

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Category Name"),
        help_text=_("format: required, max-100"),
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Category Safe URL"),
        help_text=_(
            "format: required, letters, numbers, underscore or hyphens"
        ),
    )
    is_active = models.BooleanField(default=True)

    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("Parent of Category"),
        help_text=_("format: not required"),
    )

    class MTTPMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Produt category")
        verbose_name_plural = _("Produt categories")

    def __str__(self):
        return self.name
