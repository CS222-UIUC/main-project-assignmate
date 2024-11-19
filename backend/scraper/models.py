from django.db import models
from allauth.account.models import EmailAddress

class PrairieLearnAssignment(models.Model):
    # Django-generated primary key
    id = models.AutoField(primary_key=True)
    
    # PrairieLearn-specific assignment ID (not the primary key)
    prairielearn_assignment_id = models.IntegerField(unique=True)
    
    email_address = models.ForeignKey(
        EmailAddress, 
        on_delete=models.CASCADE,
        related_name='prairielearn_assignments'
    )
    
    course_name = models.CharField(max_length=200)
    assignment_name = models.CharField(max_length=300)
    
    # Points possible for the assignment
    points_possible = models.FloatField()
    
    due_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.assignment_name} (PrairieLearn ID: {self.prairielearn_assignment_id})"
