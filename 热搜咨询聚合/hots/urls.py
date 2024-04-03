from django.urls import path
from hots import views

urlpatterns = [
       path('list/', views.index,name='首页'),
]
