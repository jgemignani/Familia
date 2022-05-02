from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    age = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.surname}'



