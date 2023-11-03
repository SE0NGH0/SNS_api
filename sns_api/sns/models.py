from django.db import models

# Create your models here.
class Sns(models.Model):
    SNSemail = models.CharField(max_length=50)
    SNSpassword = models.CharField(max_length=50)

    def __str__(self):
        return self.title
