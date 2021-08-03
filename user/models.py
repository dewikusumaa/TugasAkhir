from django.db import models

# Create your models here.
class User(models.Model):
    name        = models.CharField(max_length=200, db_index=True)
    username    = models.CharField(max_length=50, db_index=True)
    password    = models.CharField(max_length=50)
    level       = models.CharField(max_length=25)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name