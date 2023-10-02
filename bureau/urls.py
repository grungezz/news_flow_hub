from django.urls import path
from .views import index

app_name = 'bureau'

urlpatterns = [
    path("", index, name="index"),
]
