from django.db import models

# Create your models here.

class Todo(models.Model):
    created_at = models.DateTimeField()
    item = models.CharField(max_length=300)



