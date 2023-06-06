from django.db import models
from users.models import CustomUser


class Chat(models.Model):
    TEXT = 1
    FILE = 2
    STATUS = (
        (TEXT, 'TEXT'),
        (FILE, 'FILE')
    )
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, default=None)
    user_avatar = models.CharField(max_length=255, default=None)
    type = models.PositiveSmallIntegerField(choices=STATUS, blank=True, null=True, default=1)
    text = models.TextField(max_length=255)
    send_time = models.DateTimeField()
