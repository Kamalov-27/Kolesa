from django.urls import path

from . import views

urlpatterns = [
    path('favourites/', views.favorites_list),
    path('favourites/<int:favourite_id>/', views.favorites_detail),
    path('one/', views.One.as_view())
]