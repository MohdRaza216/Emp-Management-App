from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    department = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    working = models.BooleanField(default=True)

    def  __str__(self):
        return self.name
    

class Testimonial(models.Model):
    # name = models.CharField(max_length=200)
    testimonial = models.TextField()
    img = models.ImageField(upload_to = 'testimonials/')
    rating = models.IntegerField()


    def __str__(self):
        return self.testimonial
    
class Feedback(models.Model):
    name  = models.CharField(max_length=100)
    phone = models.CharField( max_length=10)
    email = models.EmailField(max_length=100)
    feedback = models.CharField(max_length=200)

    def __str__(self):
        return self.feedback

    