from django.urls import path, include
from softdesk import views
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('projects', views.ProjectViewSet)

projects_router = routers.NestedSimpleRouter(
    router,
    'projects',
    lookup='project'
    )
projects_router.register(
    'issues',
    views.IssuesViewSet,
    basename='projects-issues'
    )
projects_router.register(
    'contributors',
    views.ContributorsViewSet,
    basename='projects-contributors'
    )

urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path(
        'projects/<int:project_pk>/issues/<int:issue_pk>/comments/',
        views.CommentsList.as_view(),
        name='issues-comments'
        ),
    path(
        'projects/<int:project_pk>/issues/<int:issue_pk>/comments/<int:pk>',
        views.CommentDetail.as_view(),
        name='comment-details'
        )
]
