from rest_framework import permissions


class ModeratorPermission(permissions.BasePermission):
    """Проверка на то, что пользователь модератор."""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class OwnerPermission(permissions.BasePermission):
    """Проверка на то, что пользователь создатель курса или урока."""

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user