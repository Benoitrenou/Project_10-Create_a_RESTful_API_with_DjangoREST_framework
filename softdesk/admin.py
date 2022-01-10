from django.contrib import admin
from softdesk import models


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')


class IssueAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'tag', 'priority', )


class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'author_user_id', 'issue_id', 'created_time')


class ContributorAdmin(admin.ModelAdmin):
	list_display = ('project_id', 'user_id', 'permission', 'role')

		
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Contributor, ContributorAdmin)
