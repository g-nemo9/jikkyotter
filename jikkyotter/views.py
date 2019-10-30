from django.views import generic
from . import models
from . import forms
from jikkyotter import manage_twitter
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PostList(generic.ListView):
    """トップページのビュー。投稿一覧のような感じ"""
    model = models.Post
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-start_at']

    def get_context_data(self, *, object_list=models.Post, **kwargs):
        """SearchFormをテンプレートに渡す"""
        context = super().get_context_data()
        context['form'] = forms.SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        """フォームを利用してPostを検索"""
        form = forms.SearchForm(self.request.GET)
        form.is_valid()

        queryset = super().get_queryset()
        keyword = form.cleaned_data['keyword']
        if keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(comment__icontains=keyword)
                                       | Q(tags__name__icontains=keyword)).distinct()
        tag = form.cleaned_data['tag']
        if tag:
            queryset = queryset.filter(tags__name=tag)
        return queryset


@method_decorator(login_required, name='dispatch')
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
        context['posts'] = models.Post.objects.filter(user__pk=self.kwargs['pk'])[:5]
        context['twitter_icon'] = manage_twitter.get_twitter_bigger_icon(self.kwargs['pk'])
        return context


class UserPostList(generic.ListView):
    model = models.Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'jikkyotter/user_post_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user__pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['twitter_user'] = manage_twitter.get_twitter_user_info(self.kwargs['pk'])
        return context


class AboutView(generic.TemplateView):
    template_name = 'jikkyotter/about.html'
