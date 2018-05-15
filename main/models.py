from django.db import models

# Create your models here.
class rating(models.Model):
    class Meta():
        db_table = 'rating'
        ordering = ['id']
    name = models.CharField(max_length=100)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    def __str__(self):
        return self.name
