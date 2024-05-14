from django.urls import path
from api.views import GoogleFilesView

urlpatterns = [
    path('create-document/', GoogleFilesView.as_view(), name='create-document'),
]