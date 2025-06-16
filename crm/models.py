from django.db import models

# Create your models here.
class Membership(models.Model):
    name = models.CharField(max_length=100)
    MEMBERSHIP_CHOICES = (
        ("S", "Standard"),
        ("P", "Premium"),
        ("UX", "Ultimate Deluxe"),
    )

    membership_plan = models.CharField(
        max_length=2,
        choices=MEMBERSHIP_CHOICES,
        default="S",
    )

    membership_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    unique_code = models.CharField(
        max_length=250,
        #unique=True,
    )

    # def __str__(self):
    #     return f"{self.name} - {self.get_membership_plan_display()} ({'Active' if self.membership_active else 'Inactive'})"
    class Meta:
        verbose_name_plural = "Membership"
        ordering = ['name', 'membership_plan']
        unique_together = ('name', 'unique_code')

