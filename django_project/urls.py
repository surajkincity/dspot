"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django_project.views import home,about,contact,privacy,sitemap,google

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home , name='index'),
    url(r'^sitemap.xml/', sitemap , name='sitemap'),
    url(r'^googlefa975541a78f7cc0.html/', google , name='google'),
    url(r'^about-spotable/', about , name='about'),
    url(r'^contact-spotable/', contact , name='contact'),
    url(r'^pricavy-policy-of-spotable/', privacy , name='privacy'),


]
