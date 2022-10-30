from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCoinsPageView.as_view(), name='coins'),
    path('/detail/<pk>', views.DetailCoinsPageView.as_view(),
         name='coins-detail'),
]