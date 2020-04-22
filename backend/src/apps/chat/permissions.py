from rest_framework import permissions

class IsActive(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active


class IsVerified(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_verified