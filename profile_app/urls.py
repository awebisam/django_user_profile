from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename='api_viewset')
router.register('profile', views.UserProfileViewSet)

app_name = "profiles"

urlpatterns = [
    path("api/", views.HelloApiView.as_view(), name="hello"),
    path("login/", views.UserLoginApiView.as_view(), name="login"),
    path('', include(router.urls))
]
