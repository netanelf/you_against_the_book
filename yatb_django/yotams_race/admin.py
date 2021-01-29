from django.contrib import admin
from yotams_race.models import Recipe, Making, Comment, Source
# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'page_num', 'link',)


@admin.register(Making)
class MakingAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'timestamp', 'score', 'effort')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'timestamp',)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'link',)