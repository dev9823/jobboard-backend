from rest_framework import serializers
from .models import Applicant, Vacancy


class VacancySerializer(serializers.ModelSerializer):
    company = serializers.CharField(read_only=True)

    class Meta:
        model = Vacancy
        fields = [
            "id",
            "title",
            "company",
            "description",
            "people_to_hire",
            "salary",
            "published_at",
            "years_of_experience",
            "gender",
            "job_type",
            "deadline",
        ]

    def create(self, validated_data):
        company_id = self.context["user_id"]
        return Vacancy.objects.create(company_id=company_id, **validated_data)


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ["applicant", "vacancy", "cover_latter"]
        read_only_fields = ["applicant", "vacancy"]

    def create(self, validated_data):
        user_id = self.context.get("user_id")
        vacancy_id = self.context.get("vacancy_id")
        return Applicant.objects.create(
            applicant_id=user_id, vacancy_id=vacancy_id, **validated_data
        )
