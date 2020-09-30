from django.db import models


class Modules(models.Model):
    module_name = models.CharField(max_length=50)
    module_duaration = models.IntegerField()
    class_room = models.IntegerField()

    def __str__(self):
        return self.module_name


class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(Modules)

    def __str__(self):
        return self.name
