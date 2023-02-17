from django.db import models
class Test(models.Model):
    
    SERVICE=[
        ('service 1','Service 1'),
        ('service 2','Service 2'),
        ('service 3','Service 3'),
    ]
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    service=models.CharField(max_length=20,choices=SERVICE)
    def __str__(self):
        return self.name

     
     
