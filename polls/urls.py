from django.urls import path
# from .models import naushnik, allinfo
from .views import getnotebook, postnotebook, detail

urlpatterns=[
    path('all/', getnotebook.as_view()),
    path('detail/<int:myid>', detail),
    path('create/', postnotebook.as_view())
]