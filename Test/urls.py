from django.urls import path
from . import views

urlpatterns =[
    path('',views.String_Find,name='Test'),
    
]
