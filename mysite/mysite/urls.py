from django.conf.urls import include, url
from django.contrib import admin
from myapp import views as v 

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', v.index)
]

   