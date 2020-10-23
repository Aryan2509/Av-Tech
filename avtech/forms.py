from django import forms

from .models import Think,Video


class ThinkForm(forms.ModelForm):
	class Meta:
		model = Think
		fields = ('title' , 'author', 'summary', 'pdf')

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'videofile')