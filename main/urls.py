from django.urls import path

from . import views


urlpatterns = [
    path('one/', views.One.as_view()),
    path('cars/', views.CarViewSet.as_view({'get': 'list'})),
    path('cars/add/', views.CarViewSet.as_view({'post': 'create'})),
    path('cars/detail/<str:id>/', views.CarViewSet.as_view({'get': 'detail'})),
    path('cars/update/<str:id>/', views.CarViewSet.as_view({'post': 'update'})),
    path('cars/delete/<str:id>/', views.CarViewSet.as_view({'post': 'delete'})),
    path('city/', views.CityViewSet.as_view({'get': 'list'})),
    path('city/add/', views.CityViewSet.as_view({'post': 'create'})),
    path('city/detail/<str:id>/', views.CityViewSet.as_view({'get': 'detail'})),
    path('city/update/<str:id>/', views.CityViewSet.as_view({'post': 'update'})),
    path('city/delete/<str:id>/', views.CityViewSet.as_view({'post': 'delete'})),
    path('category/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('category/add/', views.CategoryViewSet.as_view({'post': 'create'})),
    path('category/detail/<str:id>/', views.CategoryViewSet.as_view({'get': 'detail'})),
    path('category/update/<str:id>/', views.CategoryViewSet.as_view({'post': 'update'})),
    path('category/delete/<str:id>/', views.CategoryViewSet.as_view({'post': 'delete'})),
    path('subcategory/', views.SubCategoryViewSet.as_view({'get': 'list'})),
    path('subcategory/add/', views.SubCategoryViewSet.as_view({'post': 'create'})),
    path('subcategory/detail/<str:id>/', views.SubCategoryViewSet.as_view({'get': 'detail'})),
    path('subcategory/update/<str:id>/', views.SubCategoryViewSet.as_view({'post': 'update'})),
    path('subcategory/delete/<str:id>/', views.SubCategoryViewSet.as_view({'post': 'delete'})),

]
