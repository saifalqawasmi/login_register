from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUpVIew.as_view(), name='signup'),
]

