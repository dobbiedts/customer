from django.shortcuts import render


from rest_framework import viewsets

from .serializers import accountSerializer, customerSerializer
from .models import customer_tab, account_tab


class customerViewSet(viewsets.ModelViewSet):
    queryset = customer_tab.objects.all().order_by('name', 'id')
    serializer_class = customerSerializer
 
class accountViewSet(viewsets.ModelViewSet):
    queryset = account_tab.objects.all().order_by('title')
    serializer_class = accountSerializer
