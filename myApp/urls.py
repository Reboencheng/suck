from django.conf.urls import url

from . import  views

urlpatterns = [
    url(r'^$',views.index),
    url(r'(\d+)/$',views.detail),
    url(r'^grade/$',views.grade),
    url(r'^student/$',views.student),
    url(r'^grade/(\d+)$',views.gradestudent),
]