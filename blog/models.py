from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    states=((1,"Published"),(2,"filed"),(3,"Need Edit"),(4,"Need Check"))
    status = models.IntegerField(choices=states,default=4)

    def publish(self):
            self.published_date = timezone.now()
            self.save()

    def __str__(self):
        return self.title
