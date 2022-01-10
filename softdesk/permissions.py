from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Project


class HasProjectPermissions(BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True


class HasIssuePermissions(BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)