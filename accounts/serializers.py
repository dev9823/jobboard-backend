from rest_framework import serializers
from .models import JobSeeker


class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ["user", "slug", "image", "location", "description", "resume"]
        read_only_fields = ["user", "slug"]

    # Validate the user to ensure they haven't already created an account as either a company or a job seeker
    def validate(self, attrs):
        user_id = self.context["request"].user.id
        if JobSeeker.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError("Job Seeker already exists")
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context["request"].user
        user_id = user.id
        User = self.Meta.model.user.field.related_model
        user.role = User.JOB_SEEKER
        user.save()
        return JobSeeker.objects.create(user_id=user_id, **validated_data)
