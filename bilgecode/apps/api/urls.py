from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns

import views
from django_tides.views import TideStationList, TideStationDetail

urlpatterns = patterns('',

    url(r'^passages/$', views.PassageList.as_view()),
    url(r'^passages/(?P<pk>[0-9]+)/$', views.PassageDetail.as_view(), name="passage-endpoint"),
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = format_suffix_patterns(urlpatterns)