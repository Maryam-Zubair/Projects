from django.urls import path
from .views import photo_list, photo_create

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('view/', photo_list, name='photo-list'),
    path('view/<str:name>/', photo_list, name='photo-list-by-name'),
    path('view/<int:year>/<int:month>/<int:day>/', photo_list, name='photo-list-by-date'),
    path('add/', photo_create, name='photo-create')
]