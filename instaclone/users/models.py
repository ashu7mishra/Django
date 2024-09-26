from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    phone_number = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserProfile(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False,
                                related_name='profile')

    profile_pic_url = models.ImageField(upload_to='profile_pic/', blank=True)

    bio = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=True)

    class Meta:
        unique_together = ('from_user', 'to_user')


