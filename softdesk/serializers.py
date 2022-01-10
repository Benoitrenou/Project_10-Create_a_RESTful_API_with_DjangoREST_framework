from rest_framework.serializers import ModelSerializer
from .models import Project, Issue, Comment, Contributor


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        exclude = ['author_user']
        read_field_only = ['id', 'author']


class ContributorSerializer(ModelSerializer):
    
    class Meta:
        model = Contributor
        fields = '__all__'
        read_field_only = ['id', 'project']


class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issue
        exclude = ['author_user']
        read_field_only = ['id', 'project', 'author_user', 'created_time']


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['author_user']
        read_field_only = ['id', 'author_user', 'issue', 'created_time']
