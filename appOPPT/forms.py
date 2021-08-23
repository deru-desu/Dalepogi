from django.forms import ModelForm
from .models import information, UpdateInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class StudentInfo(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentInfo, self).__init__(*args, **kwargs)

        self.fields['schedule'].widget.attrs.update(
            {'placeholder':'YYYY-MM-DD, Time (8:00 Am)'})
        
        self.fields['studentID'].widget.attrs.update(
            {'placeholder':'TUPC-XX-XXXX'})

        self.fields['name'].widget.attrs.update(
            {'placeholder':'Lastname, Firstname Middleinitial'})

        self.fields['professor'].widget.attrs.update(
            {'placeholder':'Professor/Dr. Juan'})

    class Meta:
        model = information
        fields = '__all__'

class UpdateInfo(ModelForm):
    class Meta:
        model = information
        fields = ['studentstatus', 'professor', 'school']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']