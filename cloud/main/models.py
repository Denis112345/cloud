from django.db import models
from django.urls import reverse
import os
import random
import string

# Create your models here.

class Document(models.Model):
    descriptions = models.CharField(max_length=250)
    document = models.FileField(upload_to='media/main')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL" )
    date_upload = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            letters = string.ascii_lowercase
            self.slug = ''.join(random.choice(letters) for i in range(16))
        super(Document, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('documentDownload', kwargs={'slug': self.slug})

    def get_file_url(self):
        return os.path.abspath(self.document)

    def __str__(self):
        return  self.descriptions