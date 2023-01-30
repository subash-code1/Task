from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Token(models.Model):
    number = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    current_token = models.IntegerField()
    approximate_waiting_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    doctor_name = models.CharField(max_length=255, blank=True)
    token_name =  models.CharField(max_length=255, blank=True)



