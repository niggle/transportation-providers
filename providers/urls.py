from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProviderListCreateView.as_view(), name='providers_list_create'),
    url(r'^(?P<pk>[\d]+)/$', views.ProviderRetrieveUpdateDestroyView.as_view(),
        name='providers_retrieve_update_destroy')
]
