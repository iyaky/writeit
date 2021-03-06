from .models import Challenge, ChallengeTopicName
import django_filters
from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class ChallengeFilter(django_filters.FilterSet):
    is_file_challenge = django_filters.BooleanFilter(field_name='file_challenge')
    deadline = django_filters.DateFilter(field_name='deadline', lookup_expr='lte', widget = DateInput(format='%Y-%m-%d'),
                                   input_formats=('%Y-%m-%d',))
    number_of_checks = django_filters.NumberFilter(field_name='number_of_checks', lookup_expr='lte')
    topic = django_filters.ModelMultipleChoiceFilter(field_name='topic', queryset=ChallengeTopicName.objects.all())
    class Meta:
        model = Challenge
        fields = ['topic', 'number_of_checks', 'topic' ]
