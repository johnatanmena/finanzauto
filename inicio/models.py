from django.db import models

# Create your models here.
class chatbots(models.Model):
    nombres = models.CharField(max_length = 70)
    selecc = models.CharField(max_length = 70)
    Skill = models.CharField(max_length = 70,unique=True)
    estado = models.CharField(max_length = 70)
    def __str__(self):
        return '%s' % self.nombres

class cargar(models.Model):
    nombre = models.CharField(max_length =70)
    chatbot = models.ForeignKey(chatbots, to_field='Skill', on_delete=models.CASCADE) 
    cantidad_intentos = models.IntegerField()
    def __str__(self):
        return '%s' % self.nombre




