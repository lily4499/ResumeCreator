# Generated by Django 5.0.4 on 2024-04-20 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeBuilder', '0011_auto_20210412_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='userid',
            field=models.CharField(default='default_user_id', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='areaOfInterest',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='extracurricularDetail',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='highSchoolMarks',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobDescription1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobDescription2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobDescription3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobDescription4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobDescription5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='languageDetail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='objective',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projectDescription1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projectDescription2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projectDescription3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projectDescription4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projectDescription5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skillDetail',
            field=models.TextField(),
        ),
    ]
