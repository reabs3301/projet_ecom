from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('',views.home , name = 'home'),
   path('detail/<int:prod_id>/<int:quantite>/' , views.details , name='detail'),
   path('get/<int:prod_id>/<int:client_id>/' , views.decrease , name='get'),
   path('search/', views.searching , name='search')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
