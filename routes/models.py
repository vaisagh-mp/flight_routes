from django.db import models
from django.core.exceptions import ValidationError


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Airport(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class AirportRoute(BaseModel):
    POSITION_CHOICES = (
        ('LEFT', 'Left'),
        ('RIGHT', 'Right'),
    )

    parent = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name='parent_routes'
    )
    child = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        related_name='child_routes'
    )
    position = models.CharField(max_length=5, choices=POSITION_CHOICES)
    duration = models.PositiveIntegerField(help_text="Time in minutes")

    class Meta:
        unique_together = ('parent', 'position')

    def clean(self):
        if self.parent == self.child:
            raise ValidationError("Parent and Child airport cannot be same")

    def __str__(self):
        return f"{self.parent} -> {self.child} ({self.position})"
