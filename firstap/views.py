from django.shortcuts import render
from django.http import HttpResponse

from firstap.forms import UserForm


def index(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        basket=request.POST['basket']
        vyb=request.POST['vyb']
        email=request.POST['email']
        regex=request.POST['regex']
        url_text=request.POST['url_text']
        file_path=request.POST['file_path']
        file=request.FILES['file']
        output="<h2>Пользователь</h2><h3>Имя- {0}, Возраст-{1}, Товар в корзину? {2}, Сочи? {3}, Адрес {4}, Текст {5}, URl {6}, Файл {7}, Файл {8}</h3>".format(name,age,basket,vyb,email,regex,url_text,file_path,file)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})
def about (request):
    return HttpResponse("<h2>О сайте</h2>")
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
def products(request, productid=1):
    output="<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)
def users (request,id,name):
    output ="<h2>Пользователь</h2> <h3>id: {0} Имя:{1}</h3>".format(id,name)
    return HttpResponse(output)
# Create your views here.