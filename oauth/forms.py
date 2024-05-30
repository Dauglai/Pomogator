from django.forms import ModelForm, Textarea, NumberInput
from django.forms import ModelForm, TextInput, DateTimeInput, DateInput, DateField, Textarea, NumberInput, TimeInput, \
    TimeField, EmailInput, FileInput, PasswordInput, modelformset_factory, inlineformset_factory
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'last_name': Textarea(attrs={
                'placeholder': "Фамилия",
                'class': "name-test",
                'rows': 2, 'cols': 50,
            }),
            'first_name': Textarea(attrs={
                'placeholder': "Имя",
                'class': "name-test",
                'rows': 1, 'cols': 50,
            }),
            'patronymic': Textarea(attrs={
                'class': "name-test",
                'rows': 3, 'cols': 50,
            }),
            'group': Textarea(attrs={
                'class': "name-test",
                'rows': 3, 'cols': 50,
            }),
            'vk': Textarea(attrs={
                'class': "name-test",
                'rows': 3, 'cols': 50,
            }),
            'tg': Textarea(attrs={
                'class': "name-test",
                'rows': 3, 'cols': 50,
            }),
            'birthday': DateInput(attrs={
                'placeholder': "19.12.2022"
            }),
            'gmail': EmailInput(attrs={
                'style': 'width:50px',
            })
        }