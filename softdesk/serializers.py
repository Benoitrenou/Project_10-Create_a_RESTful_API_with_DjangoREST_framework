from rest_framework.serializers import ModelSerializer
from .models import Project, Issue, Comment, Contributor


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'author_user']
        read_only_fields = ['author_user']


class ContributorSerializer(ModelSerializer):
    
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'permission', 'role', 'project']
        read_only_fields = ['project']


class IssuesSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
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

    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user', 'issue']
        read_only_fields = ['author_user', 'issue']
