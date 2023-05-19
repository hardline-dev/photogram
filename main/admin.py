from django.contrib import admin
from .models import Post, Comment, Report


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date_published',)
    list_filter = ('id', 'title', 'author', 'date_published',)

    fieldsets = (
        (None, {'fields': (
            'title', 'description', 'image', 'likes',
        )}),
        ('Owner', {'fields': (
            'author',
        )}),
        ('Date', {'fields': (
            'date_published',
        )}),
    )

    search_fields = ('id', 'title', 'author', 'date_published',)
    ordering = ('-id',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'date_published',)
    list_filter = ('id', 'post', 'author', 'date_published',)

    fieldsets = (
        (None, {'fields': (
            'post', 'comment',
        )}),
        ('Owner', {'fields': (
            'author',
        )}),
        ('Date', {'fields': (
            'date_published',
        )}),
    )

    search_fields = ('id', 'post', 'author', 'date_published',)
    ordering = ('-id',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'is_agreed', 'date_reported',)
    list_filter = ('id', 'reason', 'post', 'author', 'is_agreed', 'date_reported',)

    fieldsets = (
        (None, {'fields': (
            'reason', 'post',
        )}),
        ('Reporter', {'fields': (
            'author',
        )}),
        ('Status', {'fields': (
            'is_agreed', 'date_reported',
        )}),
    )

    search_fields = ('id', 'reason', 'post', 'author', 'date_published',)
    ordering = ('-id',)
