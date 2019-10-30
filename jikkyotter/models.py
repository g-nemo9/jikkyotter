from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from taggit.managers import TaggableManager


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta(AbstractUser.Meta):
        db_table = 'customuser'

    created_at = models.DateTimeField('登録日時', default=timezone.now)

    def __self__(self):
        return self.username


class Post(models.Model):
    """投稿モデル"""
    class Meta:
        db_table = 'post'

    title = models.CharField('タイトル', max_length=140)
    start_at = models.DateTimeField('開始日時')
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    comment = models.TextField('コメント', max_length=140, null=True, blank=True)
    tags = TaggableManager(blank=True)
    user = models.ForeignKey(CustomUser, verbose_name='投稿', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
