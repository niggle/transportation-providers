from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ServiceAreaListCreateView.as_view(), name='service_area_list_create'),
    url(r'^(?P<pk>[\d]+)/$', views.ServiceAreaRetrieveUpdateDestroyView.as_view(),
        name='service_area_retrieve_update_destroy')
]
