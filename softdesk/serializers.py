from rest_framework.serializers import ModelSerializer
from .models import Project, Issue, Comment, Contributor


class ProjectSerializer(ModelSerializer):
    """
    Handles Project serialization
    """

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user']
        read_only_fields = ['author_user']


class ContributorSerializer(ModelSerializer):
    """
    Handles Contributor serialization
    """

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'permission', 'role', 'project']
        read_only_fields = ['project']


class IssuesSerializer(ModelSerializer):
    """
    Handles Issue serialization
    """

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'tag',
            'priority',
            'status',
            'author_user',
            'assignee_user',
            'project'
            ]
        read_only_fields = ['author_user', 'project']


class CommentsSerializer(ModelSerializer):
    """
    Handles Comment serialization
    """

    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user', 'issue']
        read_only_fields = ['author_user', 'issue']
