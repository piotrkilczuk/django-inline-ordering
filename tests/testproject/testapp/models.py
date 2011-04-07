from django.db import models
from inline_ordering.models import Orderable


class Gallery(models.Model):
    
    title = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Galleries' # :)
    
    def __unicode__(self):
        return self.title


class Image(Orderable):
    
    gallery = models.ForeignKey(Gallery)
    image = models.ImageField(upload_to='testapp')
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title


class Testimonial(models.Model):
    
    gallery = models.ForeignKey(Gallery)
    title = models.CharField(max_length=200)
    content = models.TextField()