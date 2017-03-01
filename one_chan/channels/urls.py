from django.conf.urls import urls
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
    url(r'^(?P<board_name>)/$', views.board, name='board')
]