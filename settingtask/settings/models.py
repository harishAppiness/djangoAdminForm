from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ApplicationSettings(models.Model):
    id = models.AutoField(primary_key=True)
    module = models.CharField(max_length=50, null=True)
    setting_name = models.CharField(max_length=50, null=True, unique=True)
    setting_value = models.CharField(max_length=250)
    is_enabled = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])
    
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

