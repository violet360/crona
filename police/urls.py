"""police URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from fir import views as fir_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fir_view.home, name='home'),
    path('fir/new', fir_view.fir_new, name='fir_new'),
    path('fir/new/api/', fir_view.fir_new_api, name='fir_new_api'),
    path('fir/<int:pk>', fir_view.fir_detail, name = 'fir_detail'),
   	path('fir/list', fir_view.fir_list, name = 'fir_list'),
   	path('fir/enter', fir_view.fir_enter, name = 'fir_enter'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
