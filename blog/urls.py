from django.conf.urls import url
from blog.models import blog,comment
from . import views


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

]
