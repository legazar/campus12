from django.db import models

# Create your models here.
class Enspd(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_des_epreuves', null=True)
    epreuve = models.FileField(upload_to='epruve')
    correction = models.FileField(upload_to='correction')
    
    def __str__(self):
        return self.nom