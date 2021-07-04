from django.contrib import admin
from django.urls import path, include
from home import views


#DjangoAdmin Header Customization

admin.site.site_header = "login to Developer Mubashar"
admin.site.site_title = "Welcome to Mubashar's Dashboard"
admin.site.index_title = "Welcome to this portal"


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact')
]