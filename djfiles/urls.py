from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.MainPage.as_view(), name='main_page'),
    path('personal_inf/', views.PersonalInf.as_view(), name='personal_inf'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('news/', include('app_users.urls')),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('load_file/', load_file, name='load_file'),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
