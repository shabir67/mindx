from enum import Enum
from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(max_length=50)
    created_dates = models.DateTimeField(auto_now_add=True)
    updated_dates = models.DateTimeField(auto_now_add=True)
    deleted_dates = models.DateTimeField(null=True)
    status = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.email
    
    @property
    def serialize(self):
        data = {
            'id': self.id,
            'email': self.email,
            'created_dates': self.created_dates.isoformat(sep=' ', timespec='milliseconds'),
            'updated_dates': self.updated_dates.isoformat(sep=' ', timespec='milliseconds'),
            'status': self.status,
        }

        return data

class SubscribeStatus(Enum):
    subsc=1
    unsubs=0
