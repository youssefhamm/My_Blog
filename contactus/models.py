from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    numero_telephone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.nom
