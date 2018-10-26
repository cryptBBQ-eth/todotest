from django.contrib import admin
from .models import Post

#レコード表示機能
class PostAdmin(admin.ModelAdmin):
    pass
    list_display = ('message','create_date',)
    list_display_links = ('message','create_date',)

admin.site.register(Post,PostAdmin)