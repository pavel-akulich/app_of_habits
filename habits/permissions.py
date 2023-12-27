from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
    Permission class that grants access only to superusers.

    Attributes:
        message (str): A message to be displayed when the permission is not granted.
    """

    message = 'You are not a superuser!'

    def has_permission(self, request, view):
        """
        Check if the user is a superuser.
        """

        if request.user.is_superuser:
            return True
        return False


class IsOwner(BasePermission):
    """
    Permission class that grants access only to the owner of an object.

    Attributes:
        message (str): A message to be displayed when the permission is not granted.
    """

    message = 'You are not the owner!'

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is the owner of the object
        """

        if request.user == obj.user:
            return True
        return False
