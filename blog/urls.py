from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('<int:no>/', views.detail),
    path('test1/', views.test1),
    path('test2/<int:no>/', views.test2),
    path('profile/', views.profile),
    path('tag/<id>/', views.tag_list),
    path('test3/', views.test3),
]