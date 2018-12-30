from django.shortcuts import render


def index(request):
    return render(request, "survey_form.html")
