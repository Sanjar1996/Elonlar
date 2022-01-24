from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
import os, datetime, random


def upload_file_name(instance, filename):
    _, ext = os.path.splitext(filename)

    return "{}/{:%Y-%m-%d-%H-%M-%S}-{}{}".format(
        datetime.datetime.now().strftime("%Y%m"),
        datetime.datetime.now(),
        random.randint(1000, 9999), ext
    )


class User(AbstractUser):
    photo = models.ImageField()

    # def save(self, *args, **kwargs):
    #     super(*args, **kwargs)