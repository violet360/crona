from django import forms

from .models import Post
from .models import People

class PostForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea,label='content')

	class Meta:
		model = Post
		fields = ('title', 'text',)




# class People(forms.ModelForm):
# 	class Meta:
# 		model = Post
		