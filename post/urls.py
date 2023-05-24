from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('profiles/', views.profilesPage, name='profiles'),
    path('about/<int:pk>/', views.aboutdetail, name='aboutdetail'),
    path('buy/', views.buyPage, name='buy'),
    path('profile1/', views.profile1Page, name='profile1'),
    path('profile2/', views.profile2Page, name='profile2'),
    path('new/', view=views.newPostPage, name='newpage')
]