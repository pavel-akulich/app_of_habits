from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from habits.models import Award
from habits.permissions import IsOwner, IsSuperUser
from habits.serializers.award import AwardSerializer


class AwardListAPIView(generics.ListAPIView):
    """
    API view for retrieving a list of awards.

    Attributes:
        serializer_class (AwardSerializer): The serializer class for the Award model.
        queryset (QuerySet): The queryset containing all Award objects.
        permission_classes (list): The list of permission classes for the view.

    Methods:
        get_queryset(): Filters awards based on user permissions.
            For a superuser, returns all awards; for an authenticated user, returns only those belonging to the user.
    """

    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsAuthenticated | IsOwner | IsSuperUser]

    def get_queryset(self):
        """
        Filters awards based on user permissions.
        For a superuser, returns all awards; for an authenticated user, returns only those belonging to the user.

        Returns:
            QuerySet: The filtered queryset of awards.

        Raises:
            PermissionDenied: If the user is not authenticated.
        """

        user = self.request.user
        if user.is_authenticated and user.is_superuser:
            return Award.objects.all()
        elif user.is_authenticated:
            return Award.objects.filter(user=user)
        else:
            raise PermissionDenied("You are not authenticated.")


class AwardCreateAPIView(generics.CreateAPIView):
    """
    API view for creating an award.

    Attributes:
        permission_classes (list): The list of permission classes for the view.
        serializer_class (AwardSerializer): The serializer class for the Award model.

    Methods:
        perform_create(serializer): Sets the user field in the serializer to the actual authenticated user before saving
    """

    permission_classes = [IsAuthenticated]
    serializer_class = AwardSerializer

    def perform_create(self, serializer):
        """
        Sets the user field in the serializer to the current authenticated user before saving.

        Args:
            serializer (AwardSerializer): The serializer instance.
        """

        serializer.validated_data['user'] = self.request.user
        serializer.save()


class AwardUpdateAPIView(generics.UpdateAPIView):
    """
    API view for updating an award.

    Attributes:
        serializer_class (AwardSerializer): The serializer class for the Award model.
        queryset (QuerySet): The queryset containing all Award objects.
        permission_classes (list): The list of permission classes for the view.
    """

    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class AwardDestroyAPIView(generics.DestroyAPIView):
    """
    API view for deleting an award.

    Attributes:
        queryset (QuerySet): The queryset containing all Award objects.
        permission_classes (list): The list of permission classes for the view.
    """

    queryset = Award.objects.all()
    permission_classes = [IsOwner | IsSuperUser]
