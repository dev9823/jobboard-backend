from django.db import models
from django.conf import settings
from autoslug import AutoSlugField


class JobSeeker(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False,
        primary_key=True,
    )
    slug = AutoSlugField(unique=True, populate_from="user")
    image = models.ImageField(upload_to="jobseekers/images", blank=True, null=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    resume = models.FileField(upload_to="resume/")
