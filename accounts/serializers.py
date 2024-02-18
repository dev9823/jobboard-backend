from rest_framework import serializers
from .models import Company, Education, JobSeeker, Skill, WorkExperience


class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ["user", "slug", "image", "location", "description", "resume"]
        read_only_fields = ["user", "slug"]

    def validate(self, attrs):
        user_id = self.context["request"].user.id
        if JobSeeker.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError("You've already registered.")
        if Company.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError("You've registered as a Company")
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context["request"].user
        user_id = user.id
        User = self.Meta.model.user.field.related_model
        user.user_role = User.JOB_SEEKER
        user.save()
        return JobSeeker.objects.create(user_id=user_id, **validated_data)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "user",
            "name",
            "slug",
            "phone",
            "description",
            "image",
            "location",
            "industry",
            "website",
        ]
        read_only_fields = ["user", "slug"]

    def validate(self, attrs):
        user = self.context["request"].user
        user_id = user.id
        if Company.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError("You've already registered.")
        if JobSeeker.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError("You've registered as a Job Seeker")
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context["request"].user
        user_id = user.id
        User = self.Meta.model.user.field.related_model
        user.user_role = User.COMPANY
        user.save()
        return Company.objects.create(user_id=user_id, **validated_data)


class WorkExperienceSerializer(serializers.ModelSerializer):
    job_seeker = serializers.CharField(source="job_seeker.user", read_only=True)

    class Meta:
        model = WorkExperience
        fields = [
            "id",
            "job_seeker",
            "company",
            "position",
            "start_date",
            "end_date",
            "description",
        ]

    def create(self, validated_data):
        job_seeker_id = self.context["user_id"]
        return WorkExperience.objects.create(
            job_seeker_id=job_seeker_id, **validated_data
        )


class EducationSerializer(serializers.ModelSerializer):
    job_seeker = serializers.CharField(source="job_seeker.user", read_only=True)

    class Meta:
        model = Education
        fields = [
            "id",
            "job_seeker",
            "institution_name",
            "degree_name",
            "field_of_study",
            "start_date",
            "end_date",
            "description",
        ]

    def create(self, validated_data):
        job_seeker_id = self.context["user_id"]
        return Education.objects.create(job_seeker_id=job_seeker_id, **validated_data)


class SkillSerializer(serializers.ModelSerializer):
    job_seeker = serializers.CharField(source="job_seeker.user", read_only=True)

    class Meta:
        model = Skill
        fields = [
            "id",
            "job_seeker",
            "title",
            "description",
            "experience_years",
        ]

    def create(self, validated_data):
        job_seeker_id = self.context["user_id"]
        return Skill.objects.create(job_seeker_id=job_seeker_id, **validated_data)
