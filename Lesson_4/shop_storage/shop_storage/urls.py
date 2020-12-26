from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.conf import settings
import mainapp.views as mainapp

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', mainapp.ItemList.as_view(), name='index'),
    url('^add/$', mainapp.ItemCreate.as_view(), name='add_item'),
    url('^api/', include('mainapp.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
