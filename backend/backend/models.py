from django.db import models

class EmailAddress(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)
    primary = models.BooleanField(default=False)
    user_id = models.IntegerField()

    class Meta:
        db_table = 'account_emailaddress'

    def __str__(self):
        return self.email
