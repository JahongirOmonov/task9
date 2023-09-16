from .views import (GetAllNotebooks,

 PostNotebooks,

 GetDetailNotebooks, PatchNotebooks,

 DeleteNotebooks, AllFunctionNotebooks, 

PostGetNotebooks)



from .views import GetAllBolalar, GetDetailBolalar, PostBolalar, PatchBolalar, DeleteBolalar, AllFunctionBolalar, PostGetBolalar

from django.urls import path

urlpatterns=[
        path('PostGetNotebooks/', PostGetNotebooks.as_view()),
    path('AllFunctionNotebooks/<int:pk>', AllFunctionNotebooks.as_view()),



    
    path('GetAllBolalar/', GetAllBolalar.as_view()),
    path('GetDetailBolalar/<int:pk>', GetDetailBolalar.as_view()),
    path('PostBolalar/', PostBolalar.as_view() ),
    path('PatchBolalar/<int:pk>', PatchBolalar.as_view()),



    
    path('DeleteBolalar/<int:pk>', DeleteBolalar.as_view()),
    path('PostGetBolalar/', PostGetBolalar.as_view()),
    path('AllFunctionBolalar/<int:pk>', AllFunctionBolalar.as_view()),



    
    path('GetAllNotebooks/', GetAllNotebooks.as_view()),
    path('GetDetailNotebooks/<int:pk>', GetDetailNotebooks.as_view()),
    path('PostNotebooks/', PostNotebooks.as_view() ),
    path('PatchNotebooks/<int:pk>', PatchNotebooks.as_view()),



    
    path('DeleteNotebooks/<int:pk>', DeleteNotebooks.as_view()),



]