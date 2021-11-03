from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MorfisUser
class MorfisUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MorfisUser
        fields = ('username',)
class MorfisUserChangeForm(UserChangeForm):
    class Meta:
        model = MorfisUser
        fields = ('username',)