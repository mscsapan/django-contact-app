from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=120)
    
    
    def __str__(self):
        return f'{self.id} - {self.email}'
    
    class Meta:
        ordering = ['id'] #Ascending
        #ordering = ['-id'] #Descending
    