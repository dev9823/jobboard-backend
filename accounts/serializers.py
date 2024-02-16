from rest_framework import serializers
from .models import Company, JobSeeker


class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ["user", "slug", "image", "location", "description", "resume"]
        read_only_fields = ["user", "slug"]

    # Validate the user to ensure they haven't already created an account as either a company or a job seeker
    def validate(self, attrs):
        user_id = self.context["request"].user.id
        if JobSeeker.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError("You've already registered.")
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context["request"].user
        user_id = user.id
        User = self.Meta.model.user.field.related_model
        user.role = User.JOB_SEEKER
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
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context["request"].user
        user_id = user.id
        User = self.Meta.model.user.field.related_model
        user.role = User.COMPANY
        user.save()
        return Company.objects.create(user_id=user_id, **validated_data)
