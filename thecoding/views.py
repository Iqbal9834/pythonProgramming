from django.shortcuts import render
from rest_framework import viewsets
from .models import Developer,Address,Project,Block,Floorplan,People
from .serializers import Developerserializers,Addressserializers,Projectserializers,Blockserializers,Floorplanserializers,Peopleserializers
# Create your views here.

class Developerview(viewsets.ModelViewSet):
    queryset=Developer.objects.all()
    serializer_class=Developerserializers

class Addressview(viewsets.ModelViewSet):
    queryset=Address.objects.all()
    serializer_class=Addressserializers

class Projectview(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=Projectserializers

class Blockview(viewsets.ModelViewSet):
    queryset=Block.objects.all()
    serializer_class=Blockserializers

class Floorplanview(viewsets.ModelViewSet):
    queryset=Floorplan.objects.all()
    serializer_class=Floorplanserializers

class Peopleview(viewsets.ModelViewSet):
    queryset=People.objects.all()
    serializer_class=Peopleserializers