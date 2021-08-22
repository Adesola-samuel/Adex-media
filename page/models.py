from django.db import models

class WorkCategory(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class FeaturedWork(models.Model):
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='static/featured_works', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    client = models.CharField(max_length=50, default='')
    date = models.DateField(auto_now_add=True)
    url = models.URLField(default='')

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message =  models.TextField()
    email =models.EmailField()


    def __str__(self):
        return self.name
