from django.contrib import admin
from . models import UserProfile, UserToken, UserImage, ImageComment


# DOCS - https://docs.djangoproject.com/en/3.1/ref/contrib/admin/

class UserProfileAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'user', 'timestamp')

admin.site.register(UserProfile,UserProfileAdmin)


class UserTokenAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'user', 'timestamp')

admin.site.register(UserToken,UserTokenAdmin)


class UserImageAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'user', 'timestamp')

admin.site.register(UserImage,UserImageAdmin)


class ImageCommentAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'user', 'upload_description')

admin.site.register(ImageComment,ImageCommentAdmin)


