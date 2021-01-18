from django.db import models
from django.conf import settings
from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
import pytz


class Image(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    imageDescription = models.TextField(blank=True)
    copyrighted = models.BooleanField(default=True)
    hidden_to_others = models.BooleanField(default=True)
    upload_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title+" User:"+str(self.user)
