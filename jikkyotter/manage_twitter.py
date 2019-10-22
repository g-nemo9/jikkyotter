import twitter
from allauth.socialaccount.models import SocialToken
from jikkyou_project import settings
from .models import CustomUser


def get_twitter_user_info(pk):

    user = CustomUser.objects.get(pk=pk)

    consumer_key = settings.CONSUMER_KEY
    consumer_key_secret = settings.CONSUMER_KEY_SECRET
    user_object = SocialToken.objects.get(account__user=user, account__provider='twitter')
    access_token = user_object.token
    access_token_secret = user_object.token_secret

    api = twitter.Api(
        consumer_key=consumer_key,
        consumer_secret=consumer_key_secret,
        access_token_key=access_token,
        access_token_secret=access_token_secret,
    )

    twitter_user = api.UsersLookup(screen_name=user.username)[0]

    return twitter_user


def get_twitter_bigger_icon(pk):
    twitter_user = get_twitter_user_info(pk)
    nomal_url = twitter_user.profile_image_url_https
    bigger_icon = nomal_url.replace('_normal.', '_bigger.')
    return bigger_icon


def get_twitter_mini_icon(pk):
    twitter_user = get_twitter_user_info(pk)
    nomal_url = twitter_user.profile_image_url_https
    mini_icon = nomal_url.replace('_normal.', '_mini.')

    return mini_icon
