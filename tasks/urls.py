from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, JobViewSet


router = DefaultRouter()
router.register(r"tasks", TaskViewSet)
router.register(r"job", JobViewSet)

urlpatterns = [
    path("", include(router.urls))
]
