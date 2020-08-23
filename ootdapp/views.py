from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ootdapp.models import Sido, City, Image
from django.core.paginator import Paginator

def detail(request, id, like) :
    try :
        page = request.GET.get('Image.id',id)
        imageList = Image.objects.all()
        paginator = Paginator(imageList,1)
        imageListpage = paginator.get_page(page)
        imgDetail = Image.objects.get(id=id)
        context = { "imageList": imageListpage, "imgDetail": imgDetail }
        if like == 0:
            imgLike = Image.objects.get(id=id)
            imgLike.image_like += 1
            imgLike.save()
            context = { "imageList": imageListpage, "imgDetail": imgDetail, "imgLike.image_like": imgLike.image_like }
        elif like == 1:
            imgDislike = Image.image_dislike
            imgDislike.image_dislike += 1
            imgDislike.save()
            context = { "imageList": imageListpage, "imgDetail": imgDetail, "imgDislike.image_dislike": imgDislike.image_dislike }


    except Image.DoesNotExist:
        context = { "msg" : "게시물이 존재하지 않습니다." }

    return render(request, "detail.html", context)


def list(request) :
    return render(request, "list.html")