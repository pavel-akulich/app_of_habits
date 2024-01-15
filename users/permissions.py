from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission class that grants access only to the owner of an object.

    Attributes:
        message (str): A message to be displayed when the permission is not granted.

    Methods:
        has_object_permission(self, request, view, obj): Check if the user is the owner of the object.
    """

    message = 'You are not the owner!'

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is the owner of the object.

        Args:
            request (HttpRequest): The incoming HTTP request.
            view (APIView): The view associated with the request.
            obj (object): The object being accessed.

        Returns:
            bool: True if the user is the owner, False otherwise.
        """

        if request.user == obj:
            return True
        return False
