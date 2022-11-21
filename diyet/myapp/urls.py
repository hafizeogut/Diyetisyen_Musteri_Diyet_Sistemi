from django.urls import path
from.import views
#http://127.0.0.1:8000=>index
#http://127.0.0.1:8000/details =>index
#http://127.0.0.1:8000/list =>index



urlpatterns = [
    
    #dosya yolu ile viewsdeki fonksşyonlara ulaşıldı
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('details',views.details,name='details'),
    path('list',views.list,name='list'), 
    path('<int:category>',views.getProductsByCategoryID),

    path('<str:category>',views.getProductsByCategory),
]
