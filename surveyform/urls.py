from django.urls import path

from surveyform import views

app_name = 'surveyform'
urlpatterns = [
    path('', views.index, name='index'),
]
