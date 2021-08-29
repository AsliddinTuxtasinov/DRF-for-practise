from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Post,Vote



@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['post','voter']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','poster','create_at']
    search_fields = ['title']

admin.site.unregister(Group)