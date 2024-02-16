from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Company, JobSeeker
from .serializers import CompanySerializer, JobSeekerSerializer
from .permissions import IsCompany, IsJobSeeker


class JobSeekerViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        if self.request.method in ["PUT", "DELETE"]:
            return [IsJobSeeker()]
        return super().get_permissions()

    def get_serializer_context(self):
        return {"request": self.request}


class CompanyViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        if self.request.method in ["PUT", "DELETE"]:
            return [IsCompany()]
        return super().get_permissions()

    def get_serializer_context(self):
        return {"request": self.request}
