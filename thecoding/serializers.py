from rest_framework import serializers
from .models import Address,Developer,Block,Floorplan,Project,People

class Developerserializers(serializers.ModelSerializer):
    class Meta:
        model=Developer
        fields=('DevId','DevName','DevPhoneno','DevEmail','Notes','address')

class Addressserializers(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=('addressId','AddressType','Street','LandMark','Sector','City','PinCode','State')

class Projectserializers(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('ProId','projectName','projectType','NoOfTower','SiteArea','Floors','SaleRate','RentalRate','Status','CompletionYear','Powerbackup','developer','address')

class Blockserializers(serializers.ModelSerializer):
    class Meta:
        model=Block
        fields=('blockId','lifts','floors','unitavail','project')

class Floorplanserializers(serializers.ModelSerializer):
    class Meta:
        model=Floorplan
        fields=('PlanId','Configuration','SuperArea','Loading','ServantRoom','PoojaRoom','block')

class Peopleserializers(serializers.ModelSerializer):
    class Meta:
        model=People
        fields=('personId','Name','Phoneno','Email','Designation','Company','address','deve')