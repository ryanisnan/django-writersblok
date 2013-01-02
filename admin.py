from django.contrib import admin
from writersblok.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'timestamp_published')
    list_filter = ('status',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'status', 'timestamp_published')
        }),
        ('Content', {
            'fields': ('text_raw', 'text_html', 'tags')
        }),
    )

admin.site.register(Article, ArticleAdmin)
