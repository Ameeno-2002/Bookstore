from django.shortcuts import render
from .models import Textmainpg,Address,BookProduct
# from .models import Address

def index_page(request):
    textmainpg=Textmainpg.objects.first()
    address=Address.objects.first()
    try:
        bookinfo=BookProduct.objects.all()[:3]
    except:
        bookinfo=BookProduct.objects.all()
    context={'article':textmainpg,'Location': address,'bookevent':bookinfo}
    return render(request, 'index.html',context)


def shows_lists(request):
    return render(request,'shows_events.html')

def book_list(request):
    bookinfo=BookProduct.objects.all()
    context ={'bookinfo':bookinfo}
    return render(request,'productdetial.html',context)

