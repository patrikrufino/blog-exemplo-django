from django.contrib import admin
from .models import Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)
    fieldsets = (
        ('Post', {
            'fields': ('title', 'content', 'tags')
        }),
    )
    
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
  