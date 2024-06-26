from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    summary = models.TextField()
    skills = models.TextField(help_text="Separate skills with commas")
    experience = models.TextField()
    education = models.TextField()

    def __str__(self):
        return self.name
