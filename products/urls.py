
from django.urls import path, re_path
from .views import (
    home_page , HomePage,
    ProductDetailView,product_detail_view,
    HomeView,ProductView,
    ContactSummaryView,
)

app_name= 'core'

urlpatterns= [

    path('home/', home_page),
    path('homeview/', HomePage.as_view()),

    re_path('productview/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    re_path('product/(?P<pk>\d+)/$', product_detail_view),

    path('',HomeView.as_view(), name='home'),
    path('product/<pk>/', ProductView.as_view(), name='product'),

    path('contact_summary/', ContactSummaryView.as_view(), name='contactsummary'),

]