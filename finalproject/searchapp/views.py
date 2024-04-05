from django.shortcuts import render
from finalapp . models import Marvel
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    marvel=None
    query=None
    if 'q' in request.GET:
        query=request.GET('q')
        marvel=Marvel.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request,'search.html',{'query':query,'marvel':marvel})






