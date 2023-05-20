from django.db import models
from users.models import CustomUser
from base.services import get_path_file


class Task(models.Model):
    WAITING = 1
    ATWORK = 2
    ONINSPECTION = 3
    ACCEPTED = 4
    STATUS = (
        (WAITING, 'Ожидает исполнителя'),
        (ATWORK, 'В работе'),
        (ONINSPECTION, 'На проверке'),
        (ACCEPTED, 'Принят'),
    )

    task_topic = models.CharField(max_length=50)
    task_executors = models.ManyToManyField(CustomUser, default=None)
    task_number_of_performing = models.IntegerField()
    task_count_of_performing = models.IntegerField(default=0)
    task_description = models.CharField(max_length=255)
    task_deadline = models.DateTimeField()
    task_status = models.PositiveSmallIntegerField(choices=STATUS, blank=True, null=True, default=1)
    task_file = models.FileField(upload_to= get_path_file, blank=True, null=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'