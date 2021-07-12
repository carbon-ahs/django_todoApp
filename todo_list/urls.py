from django.urls import path
from . import views 

urlpatterns = [
    #path('', views., name = ''),    
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('delete/<list_id>', views.delete, name = 'delete'),
    path('cut_off/<list_id>', views.cut_off, name = 'cut_off'),
    path('uncut/<list_id>', views.uncut, name = 'uncut'),
    path('edit/<list_id>', views.edit, name = 'edit'),
    
    
]
