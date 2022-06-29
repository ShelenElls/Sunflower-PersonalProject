from django.db import models

class Status(models.Model):
    """
    The Status model provides a status to an Objective, which
    can be SUBMITTED, APPROVED, or REJECTED.

    Status is a Value Object.
    """
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)  # Default ordering for Status
        verbose_name_plural = "statuses"  # Fix the pluralization


class Objective(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    status = models.ForeignKey(
        Status,
        related_name="+",
        on_delete=models.PROTECT,
    )
    @classmethod
    def create(cls, **kwargs):
        kwargs["status"] = Status.objects.get(name="PENDING")      
        appointment = cls(**kwargs)
        appointment.save()
        return appointment

    def completed(self):
        status = Status.objects.get(name="COMPLETED")
        self.status = status
        self.save()

    def cancelled(self):
        status = Status.objects.get(name="CANCELLED")
        self.status = status
        self.save()

    def __str__(self):
        return str(self.name)
