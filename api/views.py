from rest_framework import viewsets

from .serializers import PlanSerializers

from .models import Plan
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    
class PlanCreate(CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    
class PlanDestroy(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers 
    lookup_field = 'id'       