from django import forms
from .models import Post
import bootstrap_datepicker_plus as datetimepicker


class PostForm(forms.ModelForm):
    """新規投稿のモデルフォーム"""
    class Meta:
        model = Post
        fields = ('title', 'start_at', 'comment', 'tags')
        widgets = {
            """bootstrap_datepicker_plusの設定"""
            'start_at': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }


class SearchForm(forms.Form):
    """検索フォーム"""
    keyword = forms.CharField(label='キーワード', max_length=100, required=False)
    tag = forms.CharField(label='タグ', max_length=100, required=False)
