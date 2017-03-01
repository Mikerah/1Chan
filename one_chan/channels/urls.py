from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<board_name>)[A-Za-z]+/$', views.board, name='board')
]