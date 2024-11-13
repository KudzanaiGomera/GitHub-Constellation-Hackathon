
from django.urls import path
from local_connect import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('community-hub', views.community_hub, name='community_hub'),
    path('business-profile', views.business_profile, name='business_profile'),
    path('profile', views.profile, name='profile'),
    path('events', views.events, name='events'),
    path('view-business', views.view_business, name='view_business'),
    path('payments', views.payments, name='payments')
]
