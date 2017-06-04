#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def filter_all(arg_dict,k):
    """
                {% if arg_dict.article_type_id == 0 %}
                <a class="active" href="/article-0-{{ arg_dict.category_id }}.html">全部</a>
            {% else %}
                <a href="/article-0-{{ arg_dict.category_id }}.html">全部</a>
            {% endif %}
    :param arg:
    :return:
    """
    if k == 'article_type_id':
        n1 = arg_dict["article_type_id"]
        n2 = arg_dict['category_id']
        if n1 == 0:
            ret = '<a class="active" href="/article-0-%s.html">全部</a>' % n2
        else:
            ret = '<a href="/article-0-%s.html">全部</a>' % n2
    else:
        n2 = arg_dict["article_type_id"]
        n1 = arg_dict['category_id']
        if n1 == 0:
            ret = '<a class="active" href="/article-%s-0.html">全部</a>' % n2
        else:
            ret = '<a  href="/article-%s-0.html">全部</a>' % n2
    return mark_safe(ret)


@register.simple_tag
def filter_article_type(article_type_list,arg_dict):
    """
            {% for row in article_type_list %}
                {% if row.id == arg_dict.article_type_id %}
                    <a  class="active" href="/article-{{ row.id }}-{{ arg_dict.category_id }}.html">{{ row.caption }}</a>
                {% else %}
                    <a  href="/article-{{ row.id }}-{{ arg_dict.category_id }}.html">{{ row.caption }}</a>
                {% endif %}
            {% endfor %}
    :return:
    """
    ret = []
    for row in article_type_list:
        if row.id == arg_dict['article_type_id']:
            temp = '<a  class="active" href="/article-%s-%s.html">%s</a>' %(row.id,arg_dict['category_id'],row.caption)
        else:
            temp = '<a href="/article-%s-%s.html">%s</a>' % (row.id, arg_dict['category_id'], row.caption)
        ret.append(temp)
    return mark_safe("".join(ret))