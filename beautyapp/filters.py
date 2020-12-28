import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class ServicesFilter(django_filters.FilterSet):
    
    class Meta:
        model = Services
        fields = ['services']
    services=CharFilter(field_name='services',lookup_expr='icontains')


class HairCareFilter(django_filters.FilterSet):
    
    class Meta:
        model = HairCare
        fields = ['hairCare']
    hairCare=CharFilter(field_name='hairCare',lookup_expr='icontains')

class MakeUpServicesFilter(django_filters.FilterSet):
    
    class Meta:
        model = MakeUpServices
        fields = ['makeUpServices']
    makeUpServices=CharFilter(field_name='makeUpServices',lookup_expr='icontains')

class FacialTreatmentFilter(django_filters.FilterSet):
    
    class Meta:
        model = FacialTreatment
        fields = ['facialTreatment']
    facialTreatment=CharFilter(field_name='facialTreatment',lookup_expr='icontains')

class NailArtFilter(django_filters.FilterSet):
    
    class Meta:
        model = NailArts
        fields = ['nailArts']
    nailArts=CharFilter(field_name='nailArts',lookup_expr='icontains')

class HairStyleFilter(django_filters.FilterSet):
    
    class Meta:
        model = HairStyles
        fields = ['hairStyles']
    hairStyles=CharFilter(field_name='hairStyles',lookup_expr='icontains')

class PedicureFilter(django_filters.FilterSet):
    
    class Meta:
        model = Pedicure
        fields = ['pedicure']
    pedicure=CharFilter(field_name='pedicure',lookup_expr='icontains')

class ManicureFilter(django_filters.FilterSet):
    
    class Meta:
        model = Manicure
        fields = ['manicure']
    manicure=CharFilter(field_name='manicure',lookup_expr='icontains')

class BlogFilter(django_filters.FilterSet):
    
    class Meta:
        model = Blog
        fields = ['title']
    title=CharFilter(field_name='title',lookup_expr='icontains')