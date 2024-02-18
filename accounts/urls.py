from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("job-seekers", views.JobSeekerViewSet)
router.register("company", views.CompanyViewSet)
router.register(
    "work-experience", views.WorkExperienceViewSet, basename="work-experience"
)

router.register("education", views.EducationViewSet, basename="education")
router.register("skill", views.SkillViewSet, basename="skill")
urlpatterns = router.urls
