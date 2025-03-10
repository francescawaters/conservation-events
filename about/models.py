from django.db import models

# Create your models here.


class About(models.Model):
    """
    A model to store information about the site.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
