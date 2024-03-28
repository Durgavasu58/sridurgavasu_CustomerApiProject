from django.db import models

class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number

class CustomerRecord(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)
    call_duration = models.IntegerField()
    call_type = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    week = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username} - {self.phone_number}"
