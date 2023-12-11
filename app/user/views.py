"""
Views for the user api
"""
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserViews(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
