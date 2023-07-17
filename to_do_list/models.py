from django.db import models

# Create your models here.
class Tasks(models.Model):
    tarefa = models.CharField(max_length=250)

    def __str__(self):
        return self.tarefa