from django.db import models
from django.http import request
from src import settings


class Project(models.Model):

    TYPE_OPTIONS = [
        ('Back-end', 'Back-end'),
        ('Front-end', 'Front-end'),
        ('iOS', 'iOS'),
        ('Android', 'Android')
        ]

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1064)
    type = models.CharField(choices=TYPE_OPTIONS, max_length=15 )
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='projects',
        on_delete=models.CASCADE
        )


class Contributor(models.Model):
    ROLE_OPTIONS = [
        ('Author', 'Author'),
        ('Contributor', 'Contributor')
        ]

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='contributor'
        )
    permission = models.CharField(max_length=255)
    role = models.CharField(
        default='Contributor',
        choices=ROLE_OPTIONS,
        max_length=15
        )


class Issue(models.Model):
    TAG_OPTIONS = [
        ('Bug', 'Bug'),
        ('Amélioration', 'Amélioration'),
        ('Tâche', 'Tâche')
        ]
    PRIORITY_OPTIONS = [
        ('Faible', 'Faible'),
        ('Moyenne', 'Moyenne'),
        ('Elevée', 'Elevée')
    ]
    STATUS_OPTIONS = [
        ('A faire', 'A faire'),
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé')
    ]


    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    tag = models.CharField(choices=TAG_OPTIONS, max_length=15)
    priority = models.CharField(choices=PRIORITY_OPTIONS, max_length=15)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=15)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author'
        )
    assignee_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assignee'
        )
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    description = models.CharField(max_length=255)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)