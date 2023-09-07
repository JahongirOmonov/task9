
from django.shortcuts import render, get_object_or_404
from .models import notebooks, Bolalar
from django.http import JsonResponse
from .serializer import notebooksSerializer, bolalarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def all(request):
#     all=notebooks.objects.all()
#     result=notebooksSerializer(all, many=True)
#     # for i in qoyil:
#     #     kalla.append({
#     #         'name':i.name,
#     #         'count':i.count
#     #     })
#     return JsonResponse(result.data, safe=False)

class getnotebook(APIView):
    def get(self, request):
        religion = notebooks.objects.all()
        srr=notebooksSerializer(religion, many=True)
        return Response(srr.data)
    


def detail(request, myid):
    some = Bolalar.objects.filter(id=myid)
    forgett = bolalarSerializer(some, many=True)
    # each = get_object_or_404(Bolalar, id=myid)
    # data={'name':each.name, 'number':each.number}
    return JsonResponse(forgett.data, safe=False)

class postnotebook(APIView):
    def post(self, request):
        rest=request.data
        nice = notebooksSerializer(data=rest)
        if nice.is_valid():
            nice.save()
            return Response(nice.data)
        return Response(nice.errors)
        
