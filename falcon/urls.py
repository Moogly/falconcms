from django.conf.urls import url
from django.urls import path, include

from falcon.views.home import Home

urlpatterns = [
    path('', Home.as_view()),
]
