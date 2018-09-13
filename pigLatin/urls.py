from django.conf.urls import include, url
from django.contrib import admin

# importing your views
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^translate/', views.translate, name='translate'),
    url(r'^about/', views.about, name='about'),
]
