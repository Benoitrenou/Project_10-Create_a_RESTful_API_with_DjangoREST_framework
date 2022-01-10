from rest_framework.serializers import ModelSerializer
from .models import Project, Issue, Comment, Contributor


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        read_field_only = ['id', 'author']


class ContributorSerializer(ModelSerializer):
    
    class Meta:
        model = Contributor
        fields = '__all__'
        read_field_only = ['id', 'project']


class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_field_only = ['id', 'project', 'author', 'created_time']


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_field_only = ['id', 'author', 'issue', 'created_time']
