from django.contrib import admin

from .models import Claim

class ClaimAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'list_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    list_per_page = 25

admin.site.register(Claim, ClaimAdmin)
