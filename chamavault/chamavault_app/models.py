from django.db import models

# Create your models here.

class Chamas(models.Model):
    chama_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
