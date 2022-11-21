from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

#http://127.0.0.1:8000/ 

def index(request):
    return HttpResponse('index')

def details(request):
    return HttpResponse('details')

def list(request):
    return HttpResponse('list')

def getProductsByCategoryID(request,category):
    return HttpResponse(category)

def getProductsByCategory(request,category):
    category_text=None
    if category =='bilgisayar':
        category_text="bilgisayar kategorisindeki ürünler"
    elif category=='telefon':
        category_text='telefon kategoresindeki ürünler'
    else:
        category_text='yanlış kategori seçimi'
    return HttpResponse(category_text)
    

def telefon(request):
    return HttpResponse('telefon kategorisindeki ürünler')

def bilgisayar(request):
    return HttpResponse('bilgisayar kategorisindeki ürünler')