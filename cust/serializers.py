from rest_framework import serializers

from .models import account_tab, customer_tab

class customerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = customer_tab
        fields = ('id', 'name', 'sector','industry',  'phone','email', 'gender', 'date_birth', )
        
class accountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = account_tab
        fields = '__all__'
        