from movie.models import Movie
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movie=Movie.objects.all().filter(Q(name__contains=query)|Q(genres__contains=query))
        return render(request,'search.html',{'query':query,'movie':movie})


