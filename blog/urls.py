from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('contact/', include('contactus.urls')),
    path('about/', views.about_view, name='about'),
    path('features/', views.features_view, name='features'),
    path('blog/', views.blog_view, name='blog'),
]
