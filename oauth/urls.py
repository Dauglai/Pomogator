from django.contrib import admin
from django.urls import path, include
from .endpoint import views, auth_views

login_urlpatterns = [

    path(
        "sdk/",
        include(("oauth.sdk.urls", "login-sdk")),
    ),
]

urlpatterns = [
    path("login/", include(login_urlpatterns)),
]