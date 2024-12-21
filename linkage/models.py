from django.db import models
from django.forms import ModelForm

# Create your models here.
class Linkers(models.Model):
    linkers=[
        (1,'EAAK'),
        (2,"GSGS"),
        (3,"GPGP"),
        (4,"GGGS")
      ]
    linker = models.CharField(max_length = 8, choices = linkers)

    def __str__(self):
        return self.linker
        
        

class LinkerForm(ModelForm):
    class Meta:
        model=Linkers
        fields='__all__'