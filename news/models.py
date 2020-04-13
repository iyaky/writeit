from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    posted_date = models.DateField(blank=True, default='2020-01-01', null=True) 
    body = models.TextField(default='No news')
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
