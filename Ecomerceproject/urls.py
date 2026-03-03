"""
URL configuration for Ecomerceproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from newapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('all_products/',views.all_products,name='all_products'),
    path('login/',views.sign_in,name='login'),
    path('signup/',views.register,name='signup'),
    path('logout/',views.sign_out,name='logout'),
    path('product_details/<int:id>/',views.product_details,name='product_details'),
    path('womens_details/',views.womens_details,name='womens_details.html'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)