from django.urls import path 
from hi_score import views

app_name = 'hi-score'


urlpatterns = [
    path('', views.index, name='index'),
]