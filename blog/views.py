from datetime import datetime
from django.shortcuts import redirect, render

from blog.models import Content


# Create your views here.

def index(request):
    content_list = {}
    list = Content.objects.all().order_by("ctime").reverse()
    for item in list:
        print(str(item.id) +"======" + str(item.ctime) +'\n')
    content_list["content_list"] = list
    return render(request, 'index.html', content_list)


def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content_text = request.POST.get("content_text")
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Content.objects.create(title=title, content_text=content_text, ctime=time, utime=time)
        content_list = {}
        list = Content.objects.all().order_by("ctime").reverse()
        content_list["content_list"] = list
        return redirect("/")
    if request.method == "GET":
        return render(request, "edit.html")

def artical(request):
    id = request.GET.get("page_id")
    artical = Content.objects.get(id=id)
    if artical:
        return render(request, "artical.html", {"artical":artical})
    else:
        return redirect("/")
        