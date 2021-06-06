from django.urls import path
from api.views import UserProvision

urlpatterns = [
    path('user-provision', UserProvision.as_view()),
    ]
