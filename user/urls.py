from django.urls import path
from user.views import MyView, PublisherListView

urlpatterns = [
    path("", MyView.as_view(), name="users"),
    path("publishers/", PublisherListView.as_view(), name="publishers")
]
