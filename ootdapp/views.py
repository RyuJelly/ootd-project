from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ootdapp.models import Sido, City, Image
from django.core.paginator import Paginator

def photo(request, id) :
    page = request.GET.get('Image.id',id)
    imageList = Image.objects.all()
    paginator = Paginator(imageList,1)
    imageListpage = paginator.get_page(page)
    imgDetail = Image.objects.get(id=id)
    context = { "imageList": imageListpage, "imgDetail":imgDetail }

    return render(request, "photo.html", context)


def list(request) :
    return render(request, "list.html")