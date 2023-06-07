from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(("Имя пользователя"), max_length=50)
    age = models.IntegerField(("Возраст пользователя"))
    height = models.IntegerField(("Рост пользователя"))

    def __str__(self):
        return self.name
