from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^providers/', views.ProviderListCreateView.as_view(), name='providers_list_create')

]