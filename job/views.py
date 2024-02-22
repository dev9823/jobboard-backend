from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import IsCompany
from .models import Vacancy
from .serializers import VacancySerializer


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
