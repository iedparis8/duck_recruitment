# coding=utf-8
from __future__ import unicode_literals
import django_filters
from duck_recruitment.models import Ec, CCOURS_Individu


class EcFilter(django_filters.FilterSet):
    cod_etp = django_filters.CharFilter(name='etape__cod_etp__cod_etp')
    vet = django_filters.CharFilter(name='etape__cod_vrs_vet')

    class Meta:
        model = Ec
        filter_fields = ['etape__cod_etp__cod_etp', 'etape__cod_vrs_vet', 'type_ec', 'etape']


class CcourIndividuFilter(django_filters.FilterSet):
    nom_pat = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = CCOURS_Individu
        filter_fields = ['nom_pat', 'id', 'pk', 'numero']