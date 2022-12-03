
from django.urls import path

from blog.views import artical, index, add


urlpatterns = [

    path('', index, name='index'),
    path('edit/', add, name='add'),
    path('page/', artical, name='artical'),

]