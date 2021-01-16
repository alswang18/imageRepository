from django.db import models
from django.conf import settings
from datetime import datetime
from django.conf import settings
from django.db import models


class Image(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, default=1
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    imageDescription = models.TextField(blank=True)
    upload_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title+" User:"+str(self.user)
