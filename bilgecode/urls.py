from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^_ad/', include(admin.site.urls)),

    (r'^accounts/', include('allauth.urls')),

    (r'^passage-planner/', include('bilgecode.apps.passage_planner.urls')),

    url(r'^api/', include('bilgecode.apps.api.urls')),

    url(r'^api/tides/', include('django_tides.urls')),

    # https://github.com/eldarion/django-stripe-payments
    # url(r"^payments/", include("payments.urls")),
    # url(r'^payments/', include('djstripe.urls', namespace="djstripe")),
)
