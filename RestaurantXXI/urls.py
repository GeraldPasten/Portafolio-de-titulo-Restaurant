"""RestaurantXXI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.views.static import serve
from django.urls import path,include,re_path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import Inicio,Login,logoutUsuario
from apps.restaurantApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include(('apps.usuario.urls','usuarios'))),
    path('restaurant/',include(('apps.restaurantApp.urls','restaurant'))),
    path('',Inicio.as_view(), name = 'index'),
    path('accounts/login/',Login.as_view(), name= 'login'),
    path('logout/',logoutUsuario,name ='logout'),
    path('tinymce/', include('tinymce.urls')),
    path("view-orders", views.view_orders, name="view_orders"),
    path("retrieve_saved_cart", views.retrieve_saved_cart, name="retrieve_saved_cart"),
    path("checkout", views.checkout, name="checkout"),
    path("mark_order_as_delivered", views.mark_order_as_delivered, name="mark_order_as_delivered"),
    path("save_cart", views.save_cart, name="save_cart"),
    path("check_superuser", views.check_superuser, name="check_superuser"),
    path('',include('pwa.urls')),
]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]