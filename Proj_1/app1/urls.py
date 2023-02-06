from django.urls import path
from .views import first_api, Second_api

urlpatterns = [
    path('first/', first_api),
    path('second/', Second_api.as_view())
]