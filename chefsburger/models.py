from django.db import models

# Create your models here.
class Gallery(models.Model):
    id=models.AutoField(primary_key='True', serialize = False,)
    img=models.ImageField(upload_to='dynamic_pictures')


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=200)
    message=models.TextField()


    messages="Message From"
    def __str__(self):
        return self.messages+" "+self.name