from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone_number = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    users_need = models.CharField(max_length=122)

    def __str__(self):
        return self.name
