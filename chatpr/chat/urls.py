from django.urls import path
from . import views

urlpatterns = [
    path("", views.MessageView.as_view(), name="message-viewer"),
    path("add/", views.MessageMaking.as_view(), name="Message-writer"),
]
