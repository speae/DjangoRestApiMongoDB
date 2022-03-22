from django.db import models


# Create your models here.
class Tutorial(models.Model):
    # title = models.CharField(max_length=70, blank=False, default='')
    # description = models.CharField(max_length=200,blank=False, default='')
    # published = models.BooleanField(default=False)

    title = models.CharField(max_length=70, blank=True, null=True, default='')
    description = models.TextField(max_length=200, blank=True, null=True, default='')
    # published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.description}'
