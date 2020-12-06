from django import forms
from app_users.models import News, Comment, Metatag, Picture


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'description', 'status', 'metatag']
        metatag = forms.ModelMultipleChoiceField(queryset=Metatag.objects.all(), required=False)


class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Установка необязательности - поля USER"""
        super(CommentForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields['user'].required = False
