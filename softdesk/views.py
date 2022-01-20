from django.shortcuts import get_object_or_404
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
    """
    Viewset handling Project's views
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, HasProjectPermissions]

    def get_queryset(self):
        """
        Override to filter Projects where the User is Contributor
        """
        return Project.objects.filter(contributor__user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Override to include Contributor instanciation for user
        """
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            project = serializer.save(author_user=request.user)
            Contributor.objects.create(
                user=request.user,
                project=project,
                role='Author'
                )
            return Response(serializer.data)


class ContributorsViewSet(ModelViewSet):
    """
    Viewset handling Contributor's views
    """

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, HasContributorPermissions]

    def get_queryset(self):
        """
        Override to filter Project's Contributors
        where the User is Contributor
        """
        return Contributor.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        """
        Override to include Project in Contributor instanciation
        """
        serializer = ContributorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            project = Project.objects.get(id=self.kwargs['project_pk'])
            serializer.save(project=project)
            return Response(serializer.data)


class IssuesViewSet(ModelViewSet):
    """
    Viewset handling Issue's views
    """

    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated, HasIssuePermissions]

    def get_queryset(self):
        """
        Override to filter Project's Issues
        where the User is Contributor
        """
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        """
        Override to include Project in Issue instanciation
        """
        serializer = IssuesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            project = Project.objects.get(id=self.kwargs['project_pk'])
            serializer.save(author_user=request.user, project=project)
            return Response(serializer.data)


class CommentsList(APIView):
    """
    View handling list views for Comments
    """

    permission_classes = [IsAuthenticated, HasCommentPermission]

    def get(self, request, project_pk, issue_pk, format=None):
        """
        Handles GET HTTP method for Comments
        """
        comments = Comment.objects.filter(
            issue=self.kwargs['issue_pk'],
            issue__project__pk=self.kwargs['project_pk']
            )
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, project_pk, issue_pk, format=None):
        """
        Handles POST HTTP method for Comments
        """
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            issue = Issue.objects.get(id=self.kwargs['issue_pk'])
            serializer.save(author_user=request.user, issue=issue)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    """
    View handling detail views for a Comment
    """

    permission_classes = [IsAuthenticated, HasCommentPermission]

    def get_object(self, pk):
        """
        Get Commment and verifies user's permissions
        """
        comment = get_object_or_404(
            Comment,
            id=pk,
            issue__pk=self.kwargs['issue_pk'],
            issue__project__pk=self.kwargs['project_pk']
            )
        self.check_object_permissions(self.request, comment)
        return comment

    def get(self, request, project_pk, issue_pk, pk, format=None):
        """
        Handles GET HTTP method for the Comment
        """
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def put(self, request, project_pk, issue_pk, pk, format=None):
        """
        Handles PUT HTTP method for the Comment
        """
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_pk, issue_pk, pk, format=None):
        """
        Handles DELETE HTTP method for the Comment
        """
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
