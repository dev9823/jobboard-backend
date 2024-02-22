from rest_framework_nested.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("", views.VacancyViewSet, basename="jobs")

urlpatterns = router.urls
