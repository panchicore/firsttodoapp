from django.db import models

class Todo(models.Model):
    nombre = models.CharField(max_length=512)
    descripcion = models.CharField(max_length=512)

    def __unicode__(self):
        return self.nombre

    def completed(self):
        completed = True
        for i in self.items.all():
            if i.hecha == False:
                completed = False
                break
        return completed

class TodoItem(models.Model):

    todo = models.ForeignKey(Todo, related_name='items')
    
    descripcion = models.CharField(max_length=233)
    hecha = models.BooleanField(default=False)


    def __unicode__(self):
        return self.descripcion

    def clase_css(self):
        if self.hecha:
            return "hecha"
        return ""

