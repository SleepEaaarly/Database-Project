from django.urls import path
from . import views

urlpatterns = [
    path('Login/', views.Login.as_view()),
    path('Register/', views.Register.as_view()),
    path('LookInfo/', views.LookInfo.as_view()),
    path('UpdateInfo/', views.UpdateInfo.as_view()),
    path('ChangePassword/', views.ChangePassword.as_view()),

    path('MakeResume/', views.MakeResume.as_view()),
    path('SendResume/', views.SendResume.as_view()),
    path('LookReceiveResume/', views.LookReceiveResume.as_view()),
    path('LookMyResume/', views.LookMyResume.as_view()),
    path('ChangeResumeStatus/', views.ChangeResumeStatus.as_view()),

    path('DeleteResume/', views.DeleteResume.as_view()),
    path('CreatePosition/', views.CreatePosition.as_view()),
    path('SearchPosition/', views.SearchPosition.as_view()),
    path('SearchMySendPosition/', views.SearchMySendPosition.as_view()),
    path('DeletePosition/', views.DeletePosition.as_view()),

    path('LookRegisterInfo/', views.LookRegisterInfo.as_view()),
    path('PassRegister/', views.PassRegister.as_view()),
    path('DeleteRegister/', views.DeleteRegister.as_view()),
    path('SendPost/', views.SendPost.as_view()),
    path('LookPost/', views.LookPost.as_view()),
    
    path('DeletePost/', views.DeletePost.as_view()),
    path('StatisticUserType/', views.StatisticUserType.as_view()),
    path('StatisticPlaceType/', views.StatisticPlaceType.as_view()),
    path('StatisticSalaryType/', views.StatisticSalaryType.as_view()),
    path('StatisticLabel1Type/', views.StatisticLabel1Type.as_view()),
]