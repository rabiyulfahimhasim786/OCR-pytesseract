from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dropbox/', views.DropboxList.as_view()),
    path('dropbox/<int:pk>/', views.DropboxDetail.as_view()),
    path('last/', views.last, name='last'),
    path('img/', views.imgtotext, name='last'),
]


urlpatterns = format_suffix_patterns(urlpatterns)