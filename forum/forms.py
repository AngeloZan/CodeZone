from django import forms
from forum.models import ForumPost

class NewForumPostForm(forms.Form):
    title = forms.CharField(max_length=60, required=True, label='Título')
    text = forms.CharField(max_length=10000, required=True, widget=forms.Textarea, label='Texto')

    class Meta:
        model = ForumPost
        fields = ('title', 'text')
