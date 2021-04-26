from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('add/<int:a>/<int:b>/',add,name='home'),
    path('json/<str:name>/<int:age>/',json,name='json'),
    path('second',second,name='second'),
    path('form',form,name='form'),
    path('form_submit',form_submit,name='form_submit'),
    path('form2',form2,name='form2'),
]