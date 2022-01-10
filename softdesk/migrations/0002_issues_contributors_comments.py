# Generated by Django 4.0 on 2022-01-06 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('softdesk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('tag', models.CharField(choices=[('Bug', 'Bug'), ('Amélioration', 'Amélioration'), ('Tâche', 'Tâche')], max_length=15)),
                ('priority', models.CharField(choices=[('Faible', 'Faible'), ('Moyenne', 'Moyenne'), ('Elevée', 'Elevée')], max_length=15)),
                ('status', models.CharField(choices=[('A faire', 'A faire'), ('En cours', 'En cours'), ('Terminé', 'Terminé')], max_length=15)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to='authentication.user')),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='authentication.user')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softdesk.project')),
            ],
        ),
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('Author', 'Author'), ('Contributor', 'Contributor')], default='Contributor', max_length=15)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributor', to='softdesk.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softdesk.issues')),
            ],
        ),
    ]
