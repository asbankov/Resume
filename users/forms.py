from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import ResumeModel
from django.forms import ModelForm

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class ResumeForm(ModelForm):
    class Meta:
        model = ResumeModel
        fields = ['name', 'surname', 'age', 'company', 'position', 'experience']