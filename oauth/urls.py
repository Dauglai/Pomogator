from django.contrib import admin
from django.urls import path, include


login_urlpatterns = [

    path(
        "sdk/",
        include(("oauth.sdk.urls", "login-sdk")),
    ),
]

urlpatterns = [
    path("login/", include(login_urlpatterns)),
]