import email
from django.db import models
import uuid
from datetime import datetime

# Create your models here.

class AddEmployees(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name+'_'+str(self.id)

