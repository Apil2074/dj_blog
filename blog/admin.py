from django.contrib import admin
from  blog.models import Post, Category


# Register your models here.

#for config category admin
class CatAdmin(admin.ModelAdmin):
    list_display=("title","url","cat_id",)
    search_field=('title',)


class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    # search_field=('title',)




admin.site.register(Category, CatAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(PostComment)