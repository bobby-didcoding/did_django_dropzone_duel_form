from django.db import models
from django.contrib.auth.models import User
from PIL import Image


'''
Our UserProfile model extends the built-in Django User Model
'''
class UserProfile(models.Model):
	
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	telephone = models.CharField(max_length=15, null=True, blank=True)
	address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)
	town = models.CharField(verbose_name="Town/City",max_length=100, null=True, blank=True)
	county = models.CharField(verbose_name="County",max_length=100, null=True, blank=True)
	post_code = models.CharField(verbose_name="Post Code",max_length=8, null=True, blank=True)
	country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)

	longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
	latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
	
	is_active = models.BooleanField(default = True)

	email_verified = models.BooleanField(default = False)
	has_profile = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.user}'




'''
Our UserToken model is used to store verification tokens generated by users.
'''
class UserToken(models.Model):
	
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	token = models.CharField(max_length=100, null=True, blank=True)
	
	#used to change the object type
	is_email = models.BooleanField(default= False)
	is_password = models.BooleanField(default = False)

	is_active = models.BooleanField(default = True)

	def __str__(self):
		return f'{self.user}'




'''
Our ImageComment model is used to store a comment for a group of images
'''
class ImageComment(models.Model):
	
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	upload_description = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f'{self.user}'




'''
Our UserImage model is used to store images passed through via dropzone
'''
class UserImage(models.Model):
	
	timestamp = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(verbose_name="User image", upload_to="user_images")
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	upload_description = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f'{self.user}'