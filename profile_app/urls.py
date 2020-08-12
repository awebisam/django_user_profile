from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename='api_viewset')

app_name = "profiles"

urlpatterns = [
    path("api/", views.HelloApiView.as_view(), name="hello"),
    path('', include(router.urls))
]
