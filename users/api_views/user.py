from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from habits.permissions import IsSuperUser, IsOwner
from users.models import User
from users.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for interacting with User model.

    This ViewSet provides CRUD operations for User model.

    Attributes:
        serializer_class: The serializer class used for User model.
        queryset: The queryset containing all User model instances.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        """
        Get the appropriate permissions based on the action.

        Returns:
            list: A list of permission classes.
        """

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperUser | IsOwner]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser | IsOwner]
        elif self.action == 'retrieve':
            permission_classes = [IsSuperUser | IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
