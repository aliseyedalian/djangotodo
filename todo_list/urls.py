from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about.html',views.about,name='about'),
    path('about',views.about,name='about'),
    path('delete/<item_id>',views.delete,name="delete"),
    path('undo',views.undo,name="undo"),
    path('crossoff/<item_id>',views.crossoff,name="crossoff"),
    path('uncross/<item_id>',views.uncross,name="uncross"),
    path('edit/<item_id>',views.edit,name="edit"),
]
