from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('board_list/', views.board_list), 
    path('board_detail/<int:pk>/',views.board_detail),    
]