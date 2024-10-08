import django_filters # type: ignore
from .models import *



class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created']