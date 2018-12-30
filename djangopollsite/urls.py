from django.contrib import admin
from django.urls import include, path
from polls import views


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('sf/', include('surveyform.urls')),
    path('', views.IndexView.as_view(), name='index'),
]
