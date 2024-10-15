from django.db import models
from allauth.account.models import EmailAddress

# Create your models here.
class Assignment(models.Model):
    email = models.ForeignKey(EmailAddress, on_delete=models.CASCADE, related_name='assignments')
    name = models.CharField(max_length=255)  
    course = models.CharField(max_length=255) 
    due_date = models.DateTimeField()
    platform = models.CharField(max_length=255, default="Canvas") 
    points = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.course}"
