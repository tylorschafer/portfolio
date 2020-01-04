from django.db import models

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    github = models.URLField(max_length=200, blank=True, default='')
    production = models.URLField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.title
