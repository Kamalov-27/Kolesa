from django.urls import path

from . import views


urlpatterns = [
    path('one/', views.One.as_view()),
    path('cars/', views.CarViewSet.as_view({'get': 'list'})),
    path('cars/add/', views.CarViewSet.as_view({'post': 'create'})),
]
