from django import forms
from .models import Post
from django.utils import timezone


class PostForm(forms.ModelForm):
    """新規投稿のモデルフォーム"""
    start_at = forms.DateTimeField(
        label='開始時刻',
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.now().strftime('%Y-%m-%dT%H:%M')}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Post
        fields = ('title', 'start_at', 'comment', 'tags')


class SearchForm(forms.Form):
    """検索フォーム"""
    keyword = forms.CharField(label = 'キーワード', max_length=100, required=False)
    tag = forms.CharField(label = 'タグ', max_length=100, required=False)
