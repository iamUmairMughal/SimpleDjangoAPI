from django.db import models

def upload_path(instance, filname):
    return '/'.join(['img', filname])

class Book(models.Model):
    cover = models.ImageField(upload_to=upload_path)