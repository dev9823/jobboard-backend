from django.db import models
from django.conf import settings
from autoslug import AutoSlugField


class JobSeeker(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False,
        primary_key=True,
        related_name="job_seeker",
    )
    slug = AutoSlugField(unique=True, populate_from="user")
    image = models.ImageField(upload_to="image/job_seeker", blank=True, null=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    resume = models.FileField(upload_to="resume/")


class Education(models.Model):
    job_seeker = models.ForeignKey(
        JobSeeker, on_delete=models.CASCADE, related_name="education"
    )
    institution_name = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()


class Skill(models.Model):
    job_seeker = models.ForeignKey(
        JobSeeker, on_delete=models.CASCADE, related_name="skills"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    experience_years = models.PositiveSmallIntegerField()


class WorkExperience(models.Model):
    job_seeker = models.ForeignKey(
        JobSeeker, on_delete=models.CASCADE, related_name="work_experience"
    )
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.position} at {self.company}"


class Company(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        editable=False,
        related_name="company",
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from="name")
    phone = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/company", null=True)
    location = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    industry = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"
