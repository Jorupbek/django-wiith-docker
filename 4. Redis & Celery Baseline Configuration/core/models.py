from operator import mod
from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
    