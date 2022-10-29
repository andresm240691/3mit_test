from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCoinsPageView.as_view(), name='coins'),
]