from __future__ import unicode_literals
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True,null=True)
    
    def __unicode__(self):
        return u"Note(%s,%s)" % (self.title, self.id)
        
    def get_absolute_url(self):
        return u"/note/%s/" % self.id
