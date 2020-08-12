from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.HelloApiView.as_view(), name="hello")
]
