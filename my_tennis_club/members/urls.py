from django.urls import path
from . import views

urlpatterns = [
    path('member', views.members, name='members'),
    path('stay', views.stay, name='stay'),
    path('profile', views.profile, name='profile'),
    path('portofolio', views.portofolio, name='portofolio'),
    path('uim', views.uim, name='uim'),
    path('instagram', views.instagram, name='instagram'),
    path('hadiah', views.hadiah, name='hadiah'),
]