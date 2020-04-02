from django.db import models

# Create your models here.

class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    notes = models.TextField()
    image = models.ImageField()
    due = models.DateField(null=True)