from django.db import models
from accounts.models import Company


class Vacancy(models.Model):
    MALE = "M"
    FEMALE = "F"

    GENDER_CHOICES = [(MALE, "Male"), (FEMALE, "Female")]

    FULL_TIME = "F"
    INTERN_SHIP = "I"
    CONTRACT = "C"
    REMOTE = "R"

    JOB_TYPE_CHOICES = [
        (FULL_TIME, "Full time"),
        (INTERN_SHIP, "Intern ship"),
        (CONTRACT, "Contract"),
        (REMOTE, "Remote"),
    ]
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    description = models.TextField()
    people_to_hire = models.PositiveSmallIntegerField()
    salary = models.PositiveIntegerField()
    published_at = models.DateField(auto_now_add=True)
    years_of_experience = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    job_type = models.CharField(max_length=1, choices=JOB_TYPE_CHOICES)
    deadline = models.DateField()
