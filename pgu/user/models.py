from django.db import models

# Create your models here.
class UserModel(models.Model):
    """User model for users"""
    username = models.PositiveIntegerField()
    profile_pic = models.ImageField(upload_to="profiles_pic/")

    class Meta():
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
    