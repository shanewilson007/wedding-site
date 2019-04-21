from django.contrib import admin, auth
from .models import UserFullName, RSVP, Post
from django.contrib.auth.models import User

class GuestAdmin(admin.ModelAdmin):
    list_display = ('user','reception','extra')
    search_fields = ('user','reception','extra')

class PostAdmin(admin.ModelAdmin):
    list_display = ('post','user')
    search_fields = ('user',)


admin.site.unregister(auth.models.Group)
admin.site.register(RSVP, GuestAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(UserFullName, CustomAdmin)
