from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]