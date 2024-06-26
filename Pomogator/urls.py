"""
URL configuration for Pomogator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from oauth import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from rest_framework import permissions
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from api.views import GoogleFilesView, GoogleFilesDetail
from event.views import (EventAPIList, EventAPIUpdate, EventAPIDestroy, ProjectAPIUpdate, ProjectAPIList,
                         ProjectAPIDestroy, TaskAPIList, TaskAPIUpdate, TaskAPIDestroy)
from oauth.views import ProfileAPIList,ProfileAPIUpdate, ProfileAPIDestroy, RoleViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)

router = routers.SimpleRouter()
router.register(r'role', RoleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),#http://127.0.0.1:8000/api/v1/event/
    path('accounts/profile/', ProfileAPIList.as_view()),
    path('api/v1/profile/<int:pk>/', ProfileAPIUpdate.as_view()),
    path('api/v1/profiledelete/<int:pk>/', ProfileAPIDestroy.as_view()),
    path('api/v1/event/', EventAPIList.as_view()),
    path('api/v1/event/<int:pk>/', EventAPIUpdate.as_view()),
    path('api/v1/eventdelete/<int:pk>/', EventAPIDestroy.as_view()),
    path('api/v1/project/', ProjectAPIList.as_view()),
    path('api/v1/project/<int:pk>/', ProjectAPIUpdate.as_view()),
    path('api/v1/projectdelete/<int:pk>/', ProjectAPIDestroy.as_view()),
    path('api/v1/taskdelete/<int:pk>/', TaskAPIDestroy.as_view()),
    path('api/v1/task/', TaskAPIList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/', include(('oauth.urls', "api"))),
    path('create-document/', GoogleFilesView.as_view(), name='create-document'),
    path('create-document/<int:pk>/', GoogleFilesDetail.as_view(), name='delete-document'),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]