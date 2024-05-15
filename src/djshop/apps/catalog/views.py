from django.shortcuts import render


# Create your views here.


def catalog_page(request):
    return render(request, 'base.html')

