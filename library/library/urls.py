"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from app.views import UsersCustomViewSet
from todo.views import ProjectModelViewSet, TodotModelViewSet


router = DefaultRouter()
router.register('users', UsersCustomViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', TodotModelViewSet, basename='todo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-users/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(r'^api/(?P<version>\d\.\d)/users/$', UsersCustomViewSet.as_view({'get': 'list'})),
    # path('api/users/1.0', include('app.urls', namespace='1.0')),
    # path('api/users/1.1', include('app.urls', namespace='1.1')),

]
