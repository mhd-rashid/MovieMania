from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Category
from .forms import MovieForm
# Create your views here.
def index(request):
    movie=Movie.objects.all()

    return render(request,'index.html',{'movie':movie})



def details(request,id):
    movie=Movie.objects.get(id=id)
    return render(request,'detail.html',{'movie':movie})
def add(request):
    if request.method=='POST':
        name=request.POST['movie_name']
        year=request.POST['Year']
        desc=request.POST['movie_desc']
        image=request.FILES['movie_image']
        genres=request.POST['movie_genres']
        movie=Movie(name=name,year=year,desc=desc,image=image,genres=genres)
        movie.save()
        return redirect('/')
    return render(request,'add.html',)

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'movie':movie,'form':form})
def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('details')
    return render(request,'delete.html')