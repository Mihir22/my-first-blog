from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length = 248,unique = True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    name = models.CharField(max_length = 248,unique = True)
    urls = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    t_name = models.ForeignKey(Webpage,on_delete = models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.date
