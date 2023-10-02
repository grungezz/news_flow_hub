from django.contrib import admin
from .models import Topic, Redactor, NewsPaper


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = ('username', 'years_of_experience',)


@admin.register(NewsPaper)
class NewsPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_year', 'topic',)
    filter_horizontal = ('publishers',)