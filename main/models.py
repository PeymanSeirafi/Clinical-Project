from django.db import models

class Visit(models.Model):
  full_name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=11)
  # service = models.TextChoices()
  time = models.CharField(max_length=100)

class Doctor(models.Model):
  full_name = models.CharField(max_length=100)
  desc = models.TextField()
  photo = models.ImageField(default='default-avatar.jpeg', upload_to='doctors')

class Service(models.Model):
  title = models.CharField(max_length=100)
  desc = models.TextField()
  photo = models.ImageField(upload_to='services')
