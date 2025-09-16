from rest_framework import permissions


class Moder(permissions.BasePermission):
    """Валидатор проверяет является ли пользователь модератором"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class Owner(permissions.BasePermission):
    """Валидатор проверяет является ли пользователь владельцем"""

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        else:
            return False
