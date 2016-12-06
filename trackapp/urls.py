from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trackapp import views

urlpatterns = [

    url(r'^signup/$', views.SignUpList.as_view()),
    url(r'^signup/(?P<pk>[0-9]+)/$', views.SignUpDetail.as_view()),

    # urls for home.html
    url(r'^home/$',views.home, name = 'home'),
    url(r'^$',views.home, name = 'home'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
