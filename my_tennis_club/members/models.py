from django.db import models

# Create your models here.
class member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.fisrtname} {self.lastname}"