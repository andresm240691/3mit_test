from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCoinsPageView.as_view(), name='coins'),
    path('detail/<pk>', views.DetailCoinsPageView.as_view(),
         name='coins-detail'),
    path('purchase', views.PurchaseCoinPageView.as_view(),
         name='coins-purchase'),
    path('briefcase', views.BriefCasePageView.as_view(),
         name='briefcase'),
]