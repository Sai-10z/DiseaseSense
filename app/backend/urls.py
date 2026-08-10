from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home-root'),
    path('symptoms/', views.home, name='home-symptoms'),
    path('results/',  views.home, name='home-results'),
    path('consult/',  views.home, name='home-consult'),
    path('favicon.ico', views.favicon, name='favicon'),
    path('predict/', views.predict_json, name='predict'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR.parent / 'static')
