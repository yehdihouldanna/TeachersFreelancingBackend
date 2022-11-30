import django_filters
from user_app.models import Teacher

class TeacherFilter(django_filters.FilterSet):
    disponibilities = django_filters.CharFilter(
        name='disponibilities__name',
        lookup_type='contains',
    )
    specialties = django_filters.CharFilter(
        name='specialties__name',
        lookup_type='contains',
    )
    classes = django_filters.CharFilter(
        name='classes__name',
        lookup_type='contains',
    )
    subjects = django_filters.CharFilter(
        name='subjects__name',
        lookup_type='contains',
    )

    class Meta:
        model = Teacher
        fields = ('disponibilities','classes','specialties')

