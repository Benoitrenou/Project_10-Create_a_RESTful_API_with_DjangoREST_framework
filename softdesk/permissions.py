from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Contributor, Project


class HasProjectPermissions(BasePermission):

    def has_permission(self, request, view):
        return True


    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user==obj.author_user


class HasContributorPermissions(BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        user_projects = Project.objects.filter(contributor__user=request.user)
        return project in user_projects

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)


class HasIssuePermissions(BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        user_projects = Project.objects.filter(contributor__user=request.user)
        return project in user_projects

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True


class HasCommentPermission(BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        user_projects = Project.objects.filter(contributor__user=request.user)
        return project in user_projects

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author_user==request.user
