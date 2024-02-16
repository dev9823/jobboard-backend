from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import JobSeeker
from .serializers import JobSeekerSerializer


class JobSeekerViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]

    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer

    def get_permissions(self):
        if self.request.method in ["POST", "PATCH", "DELETE"]:
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_context(self):
        return {"request": self.request}
