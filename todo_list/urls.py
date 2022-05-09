from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about.html',views.about,name='about'),
    path('about',views.about,name='about'),
    path('delete/<item_id>',views.delete,name="delete"),
    path('undo',views.undo,name="undo")
]
