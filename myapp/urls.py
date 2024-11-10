from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='product_page'),
   
    path('product/', views.book_list, name='book_list'),
]
