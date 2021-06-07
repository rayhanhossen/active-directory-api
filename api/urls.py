from django.urls import path
from api.views import UserProvision, UserDeprovision

urlpatterns = [
    path('user-provision', UserProvision.as_view()),
    path('user-deprovision', UserDeprovision.as_view()),
    ]
