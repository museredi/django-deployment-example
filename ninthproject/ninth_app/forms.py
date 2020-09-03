from django import forms
from ninth_app.models import Usersss

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Usersss
        fields = '__all__'
