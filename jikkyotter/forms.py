from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """新規投稿のモデルフォーム"""

    class Meta:
        model = Post
        fields = ('title', 'start_at', 'comment', 'tags')


class SearchForm(forms.Form):
    """検索フォーム"""
    keyword = forms.CharField(label = 'キーワード', max_length=100, required=False)
    tag = forms.CharField(label = 'タグ', max_length=100, required=False)
