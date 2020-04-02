from django.db import models

# Create your models here.

class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    notes = models.TextField(null=True)
    image = models.ImageField(null=True)
    due = models.DateField(null=True)