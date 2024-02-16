from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("job-seekers", views.JobSeekerViewSet)

urlpatterns = router.urls
