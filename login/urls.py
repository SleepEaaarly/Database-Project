from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('makeresume/', views.MakeResume.as_view()),
    path('sendresume/', views.SendResume.as_view()),
    path('lookresume/', views.LookResume.as_view()),
]