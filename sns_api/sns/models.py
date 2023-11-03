from django.db import models

# Create your models here.
class Sns(models.Model):
    SNSemail = models.CharField(max_length=15)
    SNSpassword = models.CharField(max_length=15)

    def __str__(self):
        return self.title
