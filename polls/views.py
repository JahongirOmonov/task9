
from django.shortcuts import render, get_object_or_404
from .models import notebooks, Bolalar
from django.http import JsonResponse
from .serializer import notebooksSerializer, bolalarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# # Create your views here.


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class GetAllBolalar(generics.ListAPIView):
    queryset=Bolalar.objects.all()
    serializer_class=bolalarSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return Bolalar.objects.all()

class GetDetailBolalar(generics.RetrieveAPIView):
    queryset = Bolalar.objects.all()
    serializer_class=bolalarSerializer

    # # def all(request):
# #     all=notebooks.objects.all()
# #     result=notebooksSerializer(all, many=True)
# #     # for i in qoyil:
# #     #     kalla.append({
# #     #         'name':i.name,
# #     #         'count':i.count
# #     #     })
# #     return JsonResponse(result.data, safe=False)

class PostBolalar(generics.CreateAPIView):
    queryset=Bolalar.objects.all()
    serializer_class=bolalarSerializer





class PatchBolalar(generics.UpdateAPIView):




    queryset=Bolalar.objects.all()
    serializer_class=bolalarSerializer

class DeleteBolalar(generics.DestroyAPIView):




    queryset=Bolalar.objects.all()
    serializer_class=bolalarSerializer
    # class getnotebook(APIView):
#     def get(self, request):
#         religion = notebooks.objects.all()
#         srr=notebooksSerializer(religion, many=True)
#         return Response(srr.data)
# class detailNotebook(APIView):
#     def get(self, request, *args, **kwargs):
#         x=get_object_or_404(notebooks, id=kwargs['luxid'])
#         ssc=notebooksSerializer(x)
#         return Response(ssc.data)

class PostGetBolalar(generics.ListCreateAPIView):
    queryset=Bolalar.objects.all()
    serializer_class=bolalarSerializer

class AllFunctionBolalar(generics.RetrieveUpdateDestroyAPIView):
    queryset=Bolalar.objects.all()
    serializer_class=bolalarSerializer

# # def all(request):
# #     all=notebooks.objects.all()
# #     result=notebooksSerializer(all, many=True)
# #     # for i in qoyil:
# #     #     kalla.append({
# #     #         'name':i.name,
# #     #         'count':i.count
# #     #     })
# #     return JsonResponse(result.data, safe=False)

# class getnotebook(APIView):
#     def get(self, request):
#         religion = notebooks.objects.all()
#         srr=notebooksSerializer(religion, many=True)
#         return Response(srr.data)
# class detailNotebook(APIView):
#     def get(self, request, *args, **kwargs):
#         x=get_object_or_404(notebooks, id=kwargs['luxid'])
#         ssc=notebooksSerializer(x)
#         return Response(ssc.data)
class GetAllNotebooks(generics.ListAPIView):
    queryset=notebooks.objects.all()
    serializer_class=notebooksSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return notebooks.objects.all()




class GetDetailNotebooks(generics.RetrieveAPIView):
    queryset = notebooks.objects.all()
    serializer_class=notebooksSerializer



    
# # def detail(request, myid):
# #     # some = Bolalar.objects.filter(id=myid)
# #     some=get_object_or_404(Bolalar, id=myid)
# #     forgett = bolalarSerializer(some)
# #     # each = get_object_or_404(Bolalar, id=myid)
# #     # data={'name':each.name, 'number':each.number}
# #     return JsonResponse(forgett.data, safe=False)
# class detailBolalar(APIView):
#     def get(self, request, *args, **kwargs):
#         r=get_object_or_404(Bolalar, id=kwargs['myid'])
#         s=bolalarSerializer(r)
#         return Response(s.data)

class PostNotebooks(generics.CreateAPIView):
    queryset=notebooks.objects.all()
    serializer_class=notebooksSerializer

class PatchNotebooks(generics.UpdateAPIView):
    queryset=notebooks.objects.all()
    serializer_class=notebooksSerializer
    
# class postnotebook(APIView):
#     def post(self, request):
#         rest=request.data
#         nice = notebooksSerializer(data=rest)
#         if nice.is_valid():
#             nice.save()
#             return Response(nice.data)
#         return Response(nice.errors)

class DeleteNotebooks(generics.DestroyAPIView):



    queryset=notebooks.objects.all()
    serializer_class=notebooksSerializer

class PostGetNotebooks(generics.ListCreateAPIView):
    queryset=notebooks.objects.all()
    serializer_class=notebooksSerializer

class AllFunctionNotebooks(generics.RetrieveUpdateDestroyAPIView):
    queryset=notebooks.objects.all()
    serializer_class=notebooksSerializer



    


# # def detail(request, myid):
# #     # some = Bolalar.objects.filter(id=myid)
# #     some=get_object_or_404(Bolalar, id=myid)
# #     forgett = bolalarSerializer(some)
# #     # each = get_object_or_404(Bolalar, id=myid)
# #     # data={'name':each.name, 'number':each.number}
# #     return JsonResponse(forgett.data, safe=False)
# class detailBolalar(APIView):
#     def get(self, request, *args, **kwargs):
#         r=get_object_or_404(Bolalar, id=kwargs['myid'])
#         s=bolalarSerializer(r)
#         return Response(s.data)


# class postnotebook(APIView):
#     def post(self, request):
#         rest=request.data
#         nice = notebooksSerializer(data=rest)
#         if nice.is_valid():
#             nice.save()
#             return Response(nice.data)
#         return Response(nice.errors)
        
