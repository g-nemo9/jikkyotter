from django.views import generic
from . import models
from . import forms
from jikkyotter import manage_twitter
import urllib.parse
from django.core.paginator import Paginator


class IndexView(generic.ListView):
    """トップページのビュー。投稿一覧のような感じ"""
    model = models.Post
    context_object_name = 'posts'
    paginate_by = 2


class CreatePost(generic.CreateView):
    """新規投稿のビュー。ModelFormを使う"""
    form_class = forms.PostForm
    template_name = 'jikkyotter/create.html'
    success_url = '/'

    def form_valid(self, form):
        """Postを新規作成するときにuserカラムにデータを入れる"""
        post = form.save(commit=False)
        post.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class PostDetail(generic.DetailView):
    """ 投稿詳細のビュー"""
    model = models.Post


class UserDetail(generic.DetailView):
    """ユーザー詳細のビュー"""
    model = models.CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['twitter_user'] = manage_twitter.get_twitter_user_info(self.kwargs['pk'])
        context['posts'] = models.Post.objects.filter(user__pk=self.kwargs['pk'])
        return context


class TagList(generic.ListView):
    """任意のタグを含んだ投稿一覧"""
    model = models.Post
    template_name = 'jikkyotter/tagged_post_list.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        """日本語タグをurlエンコードする"""
        context = super().get_context_data(**kwargs)
        tag_name = urllib.parse.unquote(self.kwargs['tag_name'])
        context['posts'] = models.Post.objects.filter(
            tags__name__in=tag_name.split()).order_by('-created_at')
        return context
