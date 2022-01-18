from django.contrib import admin
from softdesk import models


class ProjectAdmin(admin.ModelAdmin):
    """
    Customization of Project display in admin interface
    """
    list_display = ('pk', 'title', 'description', 'author_user')


class IssueAdmin(admin.ModelAdmin):
    """
    Customization of Issue display in admin interface
    """
    list_display = (
        'pk',
        'title',
        'description',
        'tag',
        'priority',
        'author_user'
        )
    list_filter = ['project']


class CommentAdmin(admin.ModelAdmin):
    """
    Customization of Comment display in admin interface
    """
    list_display = ('pk', 'author_user', 'issue', 'created_time')
    list_filter = ['issue']


class ContributorAdmin(admin.ModelAdmin):
    """
    Customization of Contributor display in admin interface
    """
    list_display = ('pk', 'user_id', 'project', 'permission', 'role')
    list_filter = ['project']


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Contributor, ContributorAdmin)
