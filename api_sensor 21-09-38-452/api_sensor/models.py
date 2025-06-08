from django.db import models

class LeituraSensor(models.Model):
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    umidade = models.FloatField()
    temperatura = models.FloatField()
    luminosidade = models.FloatField()  # <--- NOVO CAMPO
    irrigacao_ativa = models.BooleanField()
    nitrogenio = models.FloatField()
    fosforo = models.FloatField()
    potassio = models.FloatField()

    def __str__(self):
        return f"{self.data} {self.hora} - Temp: {self.temperatura}°C - Umid: {self.umidade}%"

