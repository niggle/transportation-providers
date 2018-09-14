from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/docs/', include_docs_urls(title='Trasportation providers api')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^providers/', include('providers.urls')),
    url(r'^service-areas/', include('service_areas.urls'))

]
