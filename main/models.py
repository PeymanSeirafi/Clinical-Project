from django.db import models

class Doctor(models.Model):
  full_name = models.CharField(max_length=100)
  desc = models.TextField()
  photo = models.ImageField(default='default-avatar.jpeg', upload_to='doctors')

  def __str__(self): return self.full_name

class Service(models.Model):
  title = models.CharField(max_length=100)
  desc = models.TextField()
  photo = models.ImageField(upload_to='services')

  def __str__(self): return self.title

class Visit(models.Model):
  full_name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=11)
  service = models.CharField(max_length=225, choices=[(obj.id, obj.title) for obj in Service.objects.all()])
  time = models.CharField(max_length=100)

  def get_choices(self): print(self.Service_Choices)