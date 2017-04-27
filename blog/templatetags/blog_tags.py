from django import template
from ..models import Post, Category

register = template.Library()


@register.assignment_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]


@register.assignment_tag
def archives():
    return Post.objects.datetimes('created_time', 'month', order='DESC')


@register.assignment_tag
def get_categorys():
    return Category.objects.all()