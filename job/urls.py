from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("", views.VacancyViewSet, basename="jobs")

vacancy_router = routers.NestedDefaultRouter(router, "", lookup="vacancy")
vacancy_router.register("applicant", views.ApplicantViewSet, basename="applicant")

urlpatterns = router.urls + vacancy_router.urls
