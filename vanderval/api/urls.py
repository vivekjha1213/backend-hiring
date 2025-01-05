from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SiteViewSet, TaskStatusAPIView

router = DefaultRouter()
router.register(r'sites', SiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('task-status/<str:task_id>/', TaskStatusAPIView.as_view(), name='task-status'),
]