from django.db import models
from django.conf import settings

# Create your models here.
class Experiment(models.Model):
    experiment_name = models.CharField(max_length=50)
    creator = models.CharField(verbose_name='username', max_length=50)

    def __str__(self):
        return self.experiment_name

class Content(models.Model):
    content_text = models.CharField(max_length=200)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    case_id = models.IntegerField('case id', default=0)

    def __str__(self):
        return self.content_text

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    value = models.BooleanField(verbose_name='confirms or not confirms')

