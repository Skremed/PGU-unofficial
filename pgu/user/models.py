if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.getcwd())
from django.db import models

# Create your models here.
class UserModel(models.Model):
    """User model for users"""
    username = models.PositiveIntegerField()
    password = models.CharField(max_length=1)
    profile_pic = models.ImageField(upload_to="profile_pics")

    class Meta():
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
    