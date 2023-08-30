
from django.shortcuts import render, get_object_or_404
from .models import notebooks, Bolalar
from django.http import JsonResponse

# Create your views here.

def all(request):
    kalla=[]
    qoyil=notebooks.objects.all()
    for i in qoyil:
        kalla.append({
            'name':i.name,
            'count':i.count
        })
    return JsonResponse(kalla, safe=False)
    


def detail(request, myid):
    each = get_object_or_404(Bolalar, id=myid)
    data={'name':each.name, 'number':each.number}
    return JsonResponse(data, safe=False)
        
