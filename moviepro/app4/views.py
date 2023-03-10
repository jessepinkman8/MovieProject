from django.shortcuts import render, HttpResponse, redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.
def demo(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'asd':movie})

def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']

        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    abc=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=abc)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'qwe':form,'asd':abc})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')