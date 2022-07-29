# Generated by Django 4.0.6 on 2022-07-28 21:00

import ckeditor.fields
import ckeditor_uploader.fields
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import simplecms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', help_text="Article's title.", max_length=200, verbose_name='Title')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, db_column='body', help_text="Article's content.", null=True, verbose_name='Body')),
                ('grid_columns', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')], db_column='grid_columns', default=12, help_text='Number of columns that the article occupies based on the Bootstrap 5 grid system.', verbose_name='Grid Columns')),
                ('article_height', models.CharField(blank=True, db_column='article_height', help_text="Article's height.", max_length=200, null=True, verbose_name='Article Height')),
                ('is_commentable', models.BooleanField(db_column='is_commentable', default=True, help_text='Is the article commentable?', verbose_name='Commentable')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, help_text='Is the article active?', verbose_name='Active')),
                ('show_title', models.BooleanField(db_column='show_title', default=True, help_text="Show the article's title?", verbose_name='Show Title')),
                ('read_more', models.BooleanField(db_column='read_more', default=False, help_text="Show the article's read more button?", verbose_name='Read More')),
                ('slug', models.SlugField(db_column='slug', help_text='URI identifier for this article', max_length=200, unique=True, verbose_name='Slug')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='date_created', help_text='Date this article was created.', verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, db_column='date_updated', help_text='Date this article was updated.', verbose_name='Date Updated')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', simplecms.models.UpperCaseCharField(db_column='name', help_text="The article type's name.", max_length=200, verbose_name='Name')),
                ('description', ckeditor.fields.RichTextField(blank=True, db_column='description', help_text="The article type's description.", null=True, verbose_name='Description')),
                ('template', models.CharField(db_column='template', default='basic.html', help_text="The template on which the article's is rendered.", max_length=200, verbose_name='Template')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, help_text='Is the article type active?', verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Article type',
                'verbose_name_plural': 'Article types',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', help_text="The image's title.", max_length=200, verbose_name='Title')),
                ('file', models.ImageField(db_column='file', help_text="The image's file.", upload_to='csm/images/', verbose_name='File')),
                ('description', ckeditor.fields.RichTextField(blank=True, db_column='description', help_text="The image's description.", null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', help_text="Page's title.", max_length=200, verbose_name='Title')),
                ('name', models.CharField(db_column='name', help_text="Page's name.", max_length=200, unique=True, verbose_name='Name')),
                ('template', models.CharField(blank=True, db_column='template', help_text="Page's template.", max_length=200, null=True, verbose_name='Template')),
                ('background_color', colorfield.fields.ColorField(blank=True, db_column='background_color', default=None, help_text='Background color of the page.', image_field=None, max_length=18, null=True, samples=None, verbose_name='Background Color')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, help_text='Is the page active?', verbose_name='Active')),
                ('slug', models.SlugField(db_column='slug', help_text='URI identifier for this page', max_length=200, unique=True, verbose_name='Slug')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='date_created', help_text='Date this page was created.', verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, db_column='date_updated', help_text='Date this page was updated.', verbose_name='Date Updated')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='PageArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(db_column='order', default=0, help_text='Order of the article in the page.', verbose_name='Order')),
                ('article', models.ForeignKey(db_column='article', help_text='Article is included in this page.', on_delete=django.db.models.deletion.DO_NOTHING, to='simplecms.article', verbose_name='Article')),
                ('page', models.ForeignKey(db_column='page', help_text='Article is included in this page.', on_delete=django.db.models.deletion.DO_NOTHING, to='simplecms.page', verbose_name='Page')),
            ],
            options={
                'verbose_name': 'Page Article',
                'verbose_name_plural': 'Page Articles',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='page',
            name='articles',
            field=models.ManyToManyField(blank=True, db_column='articles', help_text='Articles included in this page.', related_name='articles', through='simplecms.PageArticle', to='simplecms.article', verbose_name='Articles'),
        ),
        migrations.AddField(
            model_name='page',
            name='background_image',
            field=models.ForeignKey(blank=True, db_column='background_image', help_text='Background image of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='simplecms.image', verbose_name='Background Image'),
        ),
        migrations.CreateModel(
            name='MenuOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(1, 'Link'), (2, 'Submenu'), (3, 'Separator')], db_column='type', help_text='Type of the menu option.', max_length=20, verbose_name='Type')),
                ('order', models.IntegerField(db_column='order', default=0, help_text='Order of the menu option.', verbose_name='Order')),
                ('icon', models.CharField(blank=True, db_column='icon', help_text='Icon of the menu option.', max_length=200, null=True, verbose_name='Icon')),
                ('name', models.CharField(db_column='name', help_text="Menu option's name.", max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(db_column='slug', help_text='URI identifier for this menu option', max_length=200, unique=True, verbose_name='Slug')),
                ('is_active', models.BooleanField(db_column='is_active', default=True, help_text='Is the menu option active?', verbose_name='Active')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='date_created', help_text='Date this menu option was created.', verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, db_column='date_updated', help_text='Date this menu option was updated.', verbose_name='Date Updated')),
                ('page', models.ForeignKey(blank=True, db_column='page', help_text='Page of the menu option.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='simplecms.page', verbose_name='Page')),
                ('parent', models.ForeignKey(blank=True, db_column='parent', help_text='Parent of the menu option.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='simplecms.menuoption', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Menu Option',
                'verbose_name_plural': 'Menu Options',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(db_column='order', default=0, help_text='Order of the image in the article.', verbose_name='Order')),
                ('article', models.ForeignKey(db_column='article', help_text='Image is included in this article.', on_delete=django.db.models.deletion.DO_NOTHING, to='simplecms.article', verbose_name='Article')),
                ('image', models.ForeignKey(db_column='image', help_text='Image is included in this article.', on_delete=django.db.models.deletion.DO_NOTHING, to='simplecms.image', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Article Image',
                'verbose_name_plural': 'Article Images',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='background_image',
            field=models.ForeignKey(blank=True, db_column='background_image', help_text="Background image of the article's.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='simplecms.image', verbose_name='Background Image'),
        ),
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.ManyToManyField(blank=True, db_column='images', help_text="Images included in the article's.", related_name='images', through='simplecms.ArticleImage', to='simplecms.image', verbose_name='Images'),
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(db_column='type', help_text="Article's type.", on_delete=django.db.models.deletion.DO_NOTHING, to='simplecms.articletype', verbose_name='Type'),
        ),
    ]