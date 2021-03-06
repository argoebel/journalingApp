"""journalApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from journal.views import UserAPIView, UserAuthAPIView, PostAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # User URLs
    url(r'^user/create', UserAuthAPIView.as_view(), name='create_user'),
    url(r'^user/login', obtain_auth_token, name='login_user'),
    url(r'^user/logout', UserAuthAPIView.as_view(), name='logout_user'),
    path('user/<uuid:pk>', UserAPIView.as_view(), name='get_user'),
    path('user/edit/<uuid:pk>', UserAPIView.as_view(), name='edit_user'),
    path('user/delete/<uuid:pk>', UserAPIView.as_view(), name='delete_user'),

    # Post URLs
    url(r'^post/create', PostAPIView.as_view(), name='create_post'),
    path('post/edit/<uuid:pk>', PostAPIView.as_view(), name='edit_post'),
    path('post/delete/<uuid:pk>', PostAPIView.as_view(), name='delete_post'),


]
