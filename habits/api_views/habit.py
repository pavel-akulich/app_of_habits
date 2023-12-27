from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner, IsSuperUser
from habits.serializers.habit import HabitSerializer


class HabitPublicListAPIView(generics.ListAPIView):
    """
    API view for retrieving a list of public habits.

    Attributes:
        serializer_class (HabitSerializer): The serializer class for the Habit model.
        queryset (QuerySet): The queryset containing all published Habit objects.
        pagination_class (HabitPaginator): The paginator class for paginating the list.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    pagination_class = HabitPaginator


class HabitListAPIView(generics.ListAPIView):
    """
    API view for retrieving a list of habits.

    Attributes:
        serializer_class (HabitSerializer): The serializer class for the Habit model.
        queryset (QuerySet): The queryset containing all Habit objects.
        pagination_class (HabitPaginator): The paginator class for paginating the list.
        permission_classes (list): The list of permission classes for the view.

    Methods:
        get_queryset(): Filters habits based on user permissions.
            For a superuser, returns all habits; for an authenticated user, returns only those belonging to the user.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated | IsOwner | IsSuperUser]

    def get_queryset(self):
        """
        Filters habits based on user permissions.
        For a superuser, returns all habits; for an authenticated user, returns only those belonging to the user.

        Returns:
            QuerySet: The filtered queryset of habits.

        Raises:
            PermissionDenied: If the user is not authenticated.
        """

        user = self.request.user
        if user.is_authenticated and user.is_superuser:
            return Habit.objects.all()
        elif user.is_authenticated:
            return Habit.objects.filter(user=user)
        else:
            raise PermissionDenied("You are not authenticated.")


class HabitCreateAPIView(generics.CreateAPIView):
    """
    API view for creating a habit.

    Attributes:
        serializer_class (HabitSerializer): The serializer class for the Habit model.
        permission_classes (list): The list of permission classes for the view.

    Methods:
        perform_create(serializer): Sets the user field in the serializer to the actual authenticated user before saving
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Sets the user field in the serializer to the current authenticated user before saving.

        Args:
            serializer (HabitSerializer): The serializer instance.
        """

        serializer.validated_data['user'] = self.request.user
        serializer.save()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    API view for updating a habit.

    Attributes:
        serializer_class (HabitSerializer): The serializer class for the Habit model.
        queryset (QuerySet): The queryset containing all Habit objects.
        permission_classes (list): The list of permission classes for the view.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    API view for deleting a habit.

    Attributes:
        queryset (QuerySet): The queryset containing all Habit objects.
        permission_classes (list): The list of permission classes for the view.
    """

    queryset = Habit.objects.all()
    permission_classes = [IsOwner | IsSuperUser]
