from django.urls import path
from django.views.generic import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='gallery/gallery_list.html'), name='list'),
]