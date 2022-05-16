from django.db import models

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=20)
    Pnumber = models.IntegerField(null=True)
    email = models.EmailField(max_length=254)
    comment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name