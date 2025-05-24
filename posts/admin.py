from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_on')  #* Fields to display in the admin list view


#? Register the Post model with the Django admin site 
admin.site.register(Post, PostAdmin)  #* Register the Post model with the PostAdmin class

