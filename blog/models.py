from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.
import datetime
class Blog(models.Model):
    
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=4000)
    date = models.DateField( default = date.today)
    time = models.DateTimeField( default = datetime.datetime.now(),null=True)

    def __unicode__(self):
        return self.title
