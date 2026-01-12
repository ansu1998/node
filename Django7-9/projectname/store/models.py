from django.db import models
from django.contrib.auth.models import User


class Accounts(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    first_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)

# Create your models here.
class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    booked_on = models.DateField()

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
            return self.dep_name
    

class Doctors(models.Model):
    doc_name = models.CharField(max_length=200)
    doc_spec = models.TextField()
    dep_name = models.ForeignKey(Departments, on_delete = models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors', default='default_image.jpg')

    def __str__(self):
        return 'DR' +' '+ self.doc_name +' - ('+ self.doc_spec + ')'



class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Author(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
   