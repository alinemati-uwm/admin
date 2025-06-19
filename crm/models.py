from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Membership(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    MEMBERSHIP_CHOICES = (
        ("S", _("Standard")),
        ("P", _("Premium")),
        ("UX", _("Ultimate Deluxe")),
    )

    membership_plan = models.CharField(
        _("Membership Plan"),
        max_length=2,
        choices=MEMBERSHIP_CHOICES,
        default="S",
    )

    membership_active = models.BooleanField(_("Membership Active"), default=True)

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    unique_code = models.CharField(
        _("Unique Code"),
        max_length=250,
        #unique=True,
    )

    # def __str__(self):
    #     return f"{self.name} - {self.get_membership_plan_display()} ({'Active' if self.membership_active else 'Inactive'})"
    class Meta:
        verbose_name = _("Membership")
        verbose_name_plural = _("Memberships")
        ordering = ['name', 'membership_plan']
        unique_together = ('name', 'unique_code')
