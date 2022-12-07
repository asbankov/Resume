from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('editform/', ResumeView.as_view(), name='editform'),
    path('result/', ResultView.as_view(), name='result'),
    path('download/', download, name='download')
]