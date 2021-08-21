from django.urls import path
from . import views


urlpatterns = [
    path('', views.RootDocumentCreateView.as_view(), name='uploader'),
]
