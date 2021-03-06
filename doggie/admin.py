from django.contrib import admin

# Register your models here.
from django.contrib import admin
from doggie.models import DogCategory, Dog
from doggie.models import UserProfile, Comment


class DogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class DogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('dog_name',), 'dogcategory_slug': ('dogcategory',)}
    list_display = ('dog_name', 'dogcategory', 'short_description', 'views', 'likes')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'body', 'create_date','belong']

admin.site.register(DogCategory,DogCategoryAdmin)
admin.site.register(Dog,DogAdmin)
admin.site.register(UserProfile)
