from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('run', views.run,name="run"),
    path('out', views.out,name="out"),
    
    # path('output.csv/', views.download_csv,name="download_csv"),
    
    
    
]
