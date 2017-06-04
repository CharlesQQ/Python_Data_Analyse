"""s14day23 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01.views import test
from app01.views import account
from app01.views import views as view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login.html$', account.login),
    url(r'^index/$', test.register),
    url(r'^index1/$', view.index),
    url(r'^user_list/', view.user_list),
    url(r'^edit-(\d+)', view.user_edit),
    url(r'^ajax/$', view.ajax),
    url(r'^ajax_json/$', view.ajax_json),
    url(r'^upload/$', view.upload),
    url(r'^upload_file/$', view.upload_file),
    url(r'article-(?P<article_type_id>\d+)-(?P<category_id>\d+).html',view.article,name='article')   #组合搜索条件
]
