if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.getcwd())
from django import forms
from django.utils.translation import gettext_lazy
from pgu.user.models import UserModel


class UserFormModel(forms.ModelForm):
    class Meta():
        model = UserModel
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={"class":"form-control", "type":"email", "name":"email"}),
            'password': forms.TextInput(attrs={"class":"form-control", "type":"password", "name":"password"}),
        }
        labels = {
            'username': gettext_lazy(''),
            'password': gettext_lazy(''),
        }