from django.urls import include, re_path
import MyApp1.views
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


"""
django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', MyApp1.views.login, name = 'login'),
    re_path(r'home$', MyApp1.views.login, name = 'home'),
    path('index/', MyApp1.views.index, name='index'),
    path("__debug__/", include("debug_toolbar.urls")),
    path('venue.pdf', MyApp1.views.venue_pdf, name = 'venue_pdf'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    