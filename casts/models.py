from __future__ import unicode_literals

from django.db import models


class Podcasts(models.Model):
    cast = models.FileField(upload_to='mp3/', max_length=200)