from django.db import models
from django.urls import reverse
import random
import string

class Artiсles(models.Model):
    title = models.CharField('Название', max_length=50, default='Новость')
    anons = models.CharField('Анонс', max_length=250, default='Анонс')
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL",
        default=''.join(random.choice(string.ascii_lowercase) for i in range(16))
    )
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def save(self, *args, **kwargs):
        if not self.id:
            letters = string.ascii_lowercase
            self.slug = ''.join(random.choice(letters) for i in range(16))
        super(Artiсles, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('documentDownload', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title