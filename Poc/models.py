from django.db import models
Tablename=[1,'empty']
# Create your models here.
class Sample(models.Model):
    name=models.CharField(max_length=20)

    def save(self,*args,**kwargs):
        
        Tablename[0]=self.name
        return super().save(*args,**kwargs)

