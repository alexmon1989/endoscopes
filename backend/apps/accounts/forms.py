from django import forms

from apps.accounts.models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    """Форма создания пользователя в админке"""
    class Meta:
        model = CustomUser
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
