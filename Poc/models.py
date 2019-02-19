from django.db import models
Tablename=None
# Create your models here.
class Sample(models.Model):
    name=models.CharField(max_length=20)

    def save(self,*args,**kwargs):
        Tablename=self.name
        return super().save(*args,**kwargs)

