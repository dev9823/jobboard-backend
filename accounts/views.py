from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Education, JobSeeker, Skill, WorkExperience
from .serializers import (
    CompanySerializer,
    EducationSerializer,
    JobSeekerSerializer,
    SkillSerializer,
    WorkExperienceSerializer,
)
from .permissions import DenyDuplicateProfile, IsCompany, IsJobSeeker


class JobSeekerViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DenyDuplicateProfile]

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsJobSeeker()]
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id != instance.user_id:
            return Response(
                {"error": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id != instance.user_id:
            return Response(
                {"error": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def get_serializer_context(self):
        return {"request": self.request}


class CompanyViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DenyDuplicateProfile]

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsCompany()]
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id != instance.user_id:
            return Response(
                {"error": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id != instance.user_id:
            return Response(
                {"error": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def get_serializer_context(self):
        return {"request": self.request}


class WorkExperienceViewSet(ModelViewSet):
    serializer_class = WorkExperienceSerializer
    permission_classes = [IsJobSeeker]

    def get_queryset(self):
        user_id = self.request.user.id
        return WorkExperience.objects.filter(job_seeker_id=user_id)

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}


class EducationViewSet(ModelViewSet):
    serializer_class = EducationSerializer
    permission_classes = [IsJobSeeker]

    def get_queryset(self):
        user_id = self.request.user.id
        return Education.objects.filter(job_seeker_id=user_id)

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}


class SkillViewSet(ModelViewSet):
    serializer_class = SkillSerializer
    permission_classes = [IsJobSeeker]

    def get_queryset(self):
        job_seeker_id = self.request.user.id
        return Skill.objects.filter(job_seeker_id=job_seeker_id)

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
