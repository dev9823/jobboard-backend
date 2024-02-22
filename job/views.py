from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Company
from accounts.permissions import IsCompany, IsJobSeeker
from .models import Applicant, Vacancy
from .serializers import ApplicantSerializer, VacancySerializer


class VacancyViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = VacancySerializer

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            return [IsCompany()]
        return super().get_permissions()

    def get_queryset(self):
        return Vacancy.objects.filter(deadline__gt=timezone.now().date()).order_by(
            "-published_at", "-id"
        )

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id != instance.company_id:
            return Response(
                {"error": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id != instance.company_id:
            return Response(
                {"error": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


class ApplicantViewSet(ModelViewSet):
    http_method_names = ["get", "post", "delete"]
    serializer_class = ApplicantSerializer

    def get_permissions(self):
        if self.request.method in ["POST", "DELETE"]:
            return [IsJobSeeker()]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        vacancy_id = self.kwargs.get("vacancy_pk")
        if user.is_authenticated:
            if user.user_role == "CO":
                company = Company.objects.filter(user_id=user.id).first()
                return Applicant.objects.filter(
                    vacancy_id=vacancy_id, vacancy__company=company
                )
            elif user.user_role == "JS":
                return Applicant.objects.filter(
                    vacancy_id=vacancy_id, applicant_id=user.id
                )
        return Applicant.objects.none()

    def get_serializer_context(self):
        return {
            "vacancy_id": self.kwargs.get("vacancy_pk"),
            "user_id": self.request.user.id,
        }
