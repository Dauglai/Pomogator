from django.contrib import admin
from django.urls import path, include
from .endpoint import views, auth_views
from oauth.raw.apis import (
    GoogleLoginApi,
    GoogleLoginRedirectApi,
)

urlpatterns = [
    path("callback/", GoogleLoginApi.as_view(), name="callback-raw"),
    path("redirect/", GoogleLoginRedirectApi.as_view(), name="redirect-raw"),
    path('', auth_views.google_login),
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('google/', auth_views.google_auth)
]