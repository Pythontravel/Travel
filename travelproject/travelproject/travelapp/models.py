from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def _str__(self):
        return self.name


class team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def _str__(self):
        return self.name


#def _str__(self):
    #return self.name
