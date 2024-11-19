from django.db import models
from allauth.account.models import EmailAddress

class CanvasAssignment(models.Model):
    # Django-generated primary key
    id = models.AutoField(primary_key=True)
    
    # Canvas-specific assignment ID (not the primary key)
    canvas_assignment_id = models.IntegerField(unique=True)
    
    email_address = models.ForeignKey(
        EmailAddress, 
        on_delete=models.CASCADE,
        related_name='canvas_assignments'
    )
    
    course_name = models.CharField(max_length=200)
    assignment_name = models.CharField(max_length=300)
    
    # Points possible for the assignment
    points_possible = models.FloatField()
    
    due_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.assignment_name} (Canvas ID: {self.canvas_assignment_id})"
