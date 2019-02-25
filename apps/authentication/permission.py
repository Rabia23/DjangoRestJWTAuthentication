from rest_framework import permissions


class UserAccessPermission(permissions.BasePermission):
    message = 'User does not have permission for accessing this view.'

    def has_permission(self, request, view):
        return request.user.is_active
