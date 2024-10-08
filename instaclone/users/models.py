from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    phone_number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=55, null=False)
    is_active = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     abstract = True


class UserProfile(models.Model):

    DEFAULT_PROFILE_PIC_URL = "https://my_website.com/placeholder.png"

    profile_pic_url = models.CharField(max_length=255, default=DEFAULT_PROFILE_PIC_URL)
    bio = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


