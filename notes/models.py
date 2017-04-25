from __future__ import unicode_literals
import itertools
from django.utils.text import slugify

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    text = models.TextField(blank=True,null=True)
    
    def __unicode__(self):
        return u"Note(%s,%s)" % (self.title, slugify(self.title))
        
    def get_absolute_url(self):
        return u"/note/%s/" % slugify(self.title)
    
    def save(self):
      if self.instance.pk:
          return super(Note, self).save()
          
      instance = super(Note, self).save()
      instance.slug = orig = slugify(instance.title)
      
      for x in itertools.count(1):
          if not Note.objects.filter(slug=instance.slug).exists():
              break
          instance.slug = '%s-%d' % (orig, x)
          
      instance.save()
      
      return instance
