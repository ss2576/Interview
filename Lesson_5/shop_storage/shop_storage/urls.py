"""shop_storage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.conf import settings

import mainapp.views as mainapp

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', mainapp.ItemList.as_view(), name='index'),
    url('^add/$', mainapp.ItemCreate.as_view(), name='add_item'),
    url('^add_ajax/', mainapp.AddItemMixin.as_view(), name='add_ajax'),
    url('^update_items/', mainapp.ItemList.as_view(), name='update_items'),
    url('^api/', include('mainapp.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)