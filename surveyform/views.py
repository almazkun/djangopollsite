from django.views import generic


class IndexView(generic.ListView):
    template_name = 'surveyform/survey_form.html'
