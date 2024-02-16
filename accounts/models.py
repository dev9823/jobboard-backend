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
    image = models.ImageField(upload_to="image/job_seeker", blank=True, null=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    resume = models.FileField(upload_to="resume/")


class Company(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        editable=False,
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from="name")
    phone = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/company", null=True)
    location = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    industry = models.CharField(max_length=255)
