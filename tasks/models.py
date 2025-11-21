from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):

    STATUS = (
        ('doing', 'doing'),
        ('done', 'done')
    )

    STATUS_PRIOR = (
        (1,'Alta'),
        (2,'Média'),
        (3,'Baixa')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    priority = models.IntegerField(max_length=1, choices=STATUS_PRIOR, blank=False,  null=False)
    done = models.CharField(
        max_length=5,
        choices=STATUS
    )

    deadline = models.DateTimeField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
