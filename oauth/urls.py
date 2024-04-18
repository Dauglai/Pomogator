from django.contrib import admin
from django.urls import path, include
from .endpoint import views, auth_views

login_urlpatterns = [
    path(
        "raw/",
        include(("oauth.raw.urls", "login-raw")),
    ),
    path(
        "sdk/",
        include(("oauth.sdk.urls", "login-sdk")),
    ),

]

urlpatterns = [
    path("login/", include(login_urlpatterns)),
    #path('', auth_views.google_login),
   # path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    #path('google/', auth_views.google_auth),
]