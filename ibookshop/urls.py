"""ibookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import function
from shopping import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', function.home),
    path('account_create/', function.account_create),
    path('login/', function.login),
    path('shopping_basket/', function.shopping_basket),
    path('search/', function.search),
    path('checkout/', function.checkout),
    path('helpi/', function.helpi),
    path('FAQ/', function.FAQ),
    path('system/', function.system),
    path('contact/', function.contact),
    path('s_account/',function.s_account),
    path('logout/', function.logout),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
