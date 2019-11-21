from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new-card/$', views.new_card),
    url(r'^cards/(?P<card_id>\d+)/(?P<card_slug>[\w-]+)/$', views.view_card),
    url(r'^drop/$', views.drop),
    url(r'^$', views.index),
]
