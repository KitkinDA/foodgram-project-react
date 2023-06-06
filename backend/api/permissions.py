from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """
    Правило доступа, которое разрешает только автору изменять или удалять,
    остальным разрешены только безопасные методы (GET, HEAD, OPTIONS).
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class AdminOrReadOnly(permissions.BasePermission):
    """
    Правило доступа, которое разрешает только аутентифицированным
    администраторам выполнять любые действия, остальным разрешены
    только безопасные методы(GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated and request.user.is_admin)
        )
