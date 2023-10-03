from django.urls import path
from .views import (
    index,
    TopicCreateView,
)

app_name = 'bureau'

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicCreateView.as_view(), name="topic-list"),
]
