from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
import os, datetime, random


def upload_file_name(instance, filename):
    _, ext = os.path.splitext(filename)

    return "profile/{}/{:%Y-%m-%d-%H-%M-%S}-{}{}".format(
        datetime.datetime.now().strftime("%Y%m"),
        datetime.datetime.now(),
        random.randint(1000, 9999), ext
    )


class User(AbstractUser):
    photo = models.ImageField(upload_to=upload_file_name)

    def save(self, *args, **kwargs):
        if not self.photo.closed:
            img = Image.open(self.photo)
            img.thumbnail((1024,1024), Image.ANTIALIAS)

            tmp = BytesIO()
            img.save(tmp, 'PNG')

            self.photo = File(tmp, 't.png')
        return super().save(**kwargs)

    @property
    def image_url(self):
        if self.photo:
            return os.path.join(settings.MEDIA_URL, str(self.photo))
        return Path(settings.STATIC_URL).joinpath('articles/nophoto.png')