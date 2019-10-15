from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    """GETパラメーターを一部置き換える"""
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()
