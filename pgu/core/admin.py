if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.getcwd())
from django.contrib import admin
from pgu.user.models import UserModel

# Register your models here.
admin.site.register(UserModel)