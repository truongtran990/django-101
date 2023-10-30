from django.urls import path
from user.views import MyView, PublisherListView, contact

urlpatterns = [
    path("", MyView.as_view(), name="users"),
    path("publishers/", PublisherListView.as_view(), name="publishers"),
    path("contact/", contact, name="contact"),
]
