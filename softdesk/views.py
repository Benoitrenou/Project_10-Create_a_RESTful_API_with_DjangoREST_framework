from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Contributor, Issue, Project, Comment
from .serializers import CommentsSerializer, ContributorSerializer,\
    IssuesSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import HasCommentPermission, HasContributorPermissions,\
    HasIssuePermissions, HasProjectPermissions
from rest_framework.response import Response
from rest_framework import status


class ProjectViewSet(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, HasProjectPermissions]

    def get_queryset(self):
        return Project.objects.filter(contributor__user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            project = serializer.save(author_user=request.user)
            Contributor.objects.create(user=request.user, project=project, role='Author')
            return Response(serializer.data)


class ContributorsViewSet(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, HasContributorPermissions]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        serializer = ContributorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            project = Project.objects.get(id=self.kwargs['project_pk'])
            serializer.save(project=project)
            return Response(serializer.data)


class IssuesViewSet(ModelViewSet):

    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated, HasIssuePermissions]

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        serializer = IssuesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            project = Project.objects.get(id=self.kwargs['project_pk'])
            serializer.save(author_user=request.user, project=project)
            return Response(serializer.data)


class CommentsList(APIView):

    permission_classes = [IsAuthenticated, HasCommentPermission]

    def get(self, request, project_pk, issue_pk, format=None):
        comments = Comment.objects.filter(issue=self.kwargs['issue_pk'])
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, project_pk, issue_pk, format=None):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            issue = Issue.objects.get(id=self.kwargs['issue_pk'])
            serializer.save(author_user=request.user, issue=issue)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    permission_classes = [IsAuthenticated, HasCommentPermission]

    def get_object(self, pk):
        try:
            comment = Comment.objects.get(id=pk)
        except Comment.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, comment)
        return comment

    def get(self, request, project_pk, issue_pk, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def put(self, request, project_pk, issue_pk, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_pk, issue_pk, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
