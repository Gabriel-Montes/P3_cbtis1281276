from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('con/',views.con,name='con'),
    path('emp/',views.emp,name='emp'),
    path('suc/',views.suc,name='suc'),
    path('pro/',views.pro,name='pro'),
    path('cli/',views.cli,name='cli'),
]
