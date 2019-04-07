from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('makeSurvey',views.makeSurvey, name='makeSurvey'),
    path('allSurvey', views.allSurvey, name='allSurvey'),
    path('makeQuestion/<int:pk>/',views.makeQuestion, name='makeQuestion'),



]
