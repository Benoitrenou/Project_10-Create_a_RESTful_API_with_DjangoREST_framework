from django.urls import path, include
from softdesk import views
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('projects', views.ProjectViewSet)

projects_router = routers.NestedSimpleRouter(router, 'projects', lookup='project')
projects_router.register('issues', views.IssuesViewSet, basename='projects-issues')
projects_router.register('contributors', views.ContributorsViewSet, basename='projects-contributors')

#issues_router = routers.NestedSimpleRouter(projects_router, 'issues', lookup='issue')
#issues_router.register('comments', views.CommentsViewSet, basename='issues-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('projects-issues/comments', views.CommentsList.as_view(), name='issues-comments'),
    #path('projects/<int:pk>/issues/<int:pk>/comments/<int:pk>', views.CommentDetail.as_view(), name='comment-details')
    #path('', include(issues_router.urls)),

]