from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    """新規投稿のモデルフォーム"""

    class Meta:
        model = Post
        fields = ('title', 'start_at', 'comment', 'tags')
