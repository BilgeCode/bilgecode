from django.conf.urls import patterns, include, url

from views import PlannerHome, PassageNew, PassageDemo, PassageDetail, PassageDelete

urlpatterns = patterns('',
    url(r'^$', PlannerHome.as_view(), name='planner-home'),
    url(r'^demo/$', PassageDemo.as_view(), name='planner-demo'),
    url(r'^new/$', PassageNew.as_view(), name='planner-new'),
    url(r'^(?P<slug>[^/]+)/$', PassageDetail.as_view(), name='planner-detail'),
    url(r'^(?P<slug>[^/]+)/delete/$', PassageDelete.as_view(), name='planner-delete'),
)


