from django.urls import path

from . import views

urlpatterns = [
    path('one/', views.One.as_view())
]