from django.urls import path

from . import views

app_name = 'surveyform'
urlpatterns = [
    path('sf/', views.IndexView.as_view(), name='survey_form')
]