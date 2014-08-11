from django.contrib import admin

from models import Passage

class PassageAdmin(admin.ModelAdmin):
    list_display = ('hash_key', 'user', 'date_created')
    search_fields = ('user__email', 'user__username')
admin.site.register(Passage, PassageAdmin)