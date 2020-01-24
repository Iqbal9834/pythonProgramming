from django.db import models


# Create your models here.
class Address(models.Model):
    addressId=models.AutoField(primary_key=True)
    AddressType=models.TextField()
    Street=models.CharField(max_length=200)
    LandMark=models.CharField(max_length=80)
    Sector=models.CharField(max_length=80)
    City=models.CharField(max_length=50)
    PinCode=models.PositiveIntegerField()
    State=models.CharField(max_length=50)
    def __str__(self):
        string="|{:^10}|{:^10}|{:^10}|{:^10}|".format(self.AddressType,self.Street,self.State,self.LandMark) 
        return string

class Developer(models.Model):
    DevId=models.AutoField(primary_key=True)
    DevName=models.CharField(max_length=20)
    DevPhoneno=models.PositiveIntegerField()
    DevEmail=models.EmailField(max_length=40)
    Notes=models.TextField()
    address=models.OneToOneField(Address,on_delete=models.CASCADE)
    def __str__(self):
        string="|{:^10}|{:^10}|{:^10}|{:^10}|".format(self.DevName,self.DevPhoneno,self.DevEmail,self.Notes) 
        return string

class Project(models.Model):
    ProId=models.AutoField(primary_key=True)
    projectName=models.CharField(max_length=100)
    projectType=models.TextField()
    NoOfTower=models.PositiveIntegerField()
    SiteArea=models.FloatField()
    Floors=models.PositiveIntegerField()
    SaleRate=models.FloatField()
    RentalRate=models.FloatField()
    Status=models.BooleanField()
    CompletionYear=models.PositiveIntegerField()
    Powerbackup=models.PositiveIntegerField()
    developer=models.ForeignKey(Developer,on_delete=models.CASCADE)
    address=models.OneToOneField(Address, on_delete=models.CASCADE)
    def __str__(self):
        string="|{:^10}|{:^10}|".format(self.projectName,self.projectType) 
        return string
   
class Block(models.Model):
    blockId=models.AutoField(primary_key=True)
    lifts=models.BooleanField()
    floors=models.PositiveIntegerField()
    unitavail=models.PositiveIntegerField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    def __str__(self):
        string="|{:^10}|{:^10}||{:^10}|".format(self.lifts,self.floors,self.unitavail) 
        return string
   

class Floorplan(models.Model):
    PlanId=models.AutoField(primary_key=True)
    Configuration=models.CharField(max_length=10)
    SuperArea=models.FloatField()
    Loading=models.FloatField()
    ServantRoom=models.BooleanField()
    PoojaRoom=models.BooleanField()
    block=models.ForeignKey(Block,on_delete=models.CASCADE)
    def __str__(self):
        string="|{:^10}|{:^10}||{:^10}|{:^10}|{:^10}||{:^10}|".format(self.PlanId,self.Configuration,self.SuperArea,self.Loading,self.ServantRoom,self.PoojaRoom) 
        return string
    

class People(models.Model):
    personId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=20)
    Phoneno=models.PositiveIntegerField()
    Email=models.EmailField()
    Designation=models.CharField(max_length=100)
    Company=models.CharField(max_length=80)
    address=models.OneToOneField(Address,on_delete=models.CASCADE)
    deve=models.ForeignKey(Developer,on_delete=models.CASCADE)
    def __str__(self):
        string="|{:^10}|{:^10}||{:^10}|{:^10}|{:^10}|".format(self.Name,self.Phoneno,self.Email,self.Designation,self.Company) 
        return string
    

  