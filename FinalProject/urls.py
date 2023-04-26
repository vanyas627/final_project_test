"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from main_app.views import main_view
from manager.views import  manager_view, manager_booked_view, update_booked_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('manager/', manager_view),
    path('manager/message_delet.html/', include('manager.urls', namespace='manager/message_delet.html/')),
    path('manager/message_delet.html/update/', include('manager.urls', namespace='manager/message_delet.html/update/')),
    path('manager/message.html/', include('manager.urls_2', namespace='manager/message.html/')),
    path('manager/message.html/update/', include('manager.urls_2', namespace='manager/message.html/update/'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)