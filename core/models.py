from django.db import models

# Create your models here.

class Profession(models.Model): 
    description = models.CharField(max_length=50)
class DataSheet(models.Model): 
    description = models.CharField(max_length=50)
    historical_data = models.CharField(max_length=50)
class Customer(models.Model): 
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    profession = models.ManyToManyField(Profession)
    datasheet = models.OneToOneField(DataSheet, on_delete=models.CASCADE,primary_key=True)        
    def __str(self): 
        return self.name

class Document(models.Model): 
    PP = 'PP'
    ID = 'ID'
    OT = 'OT'
    DOC_TYPES = [
        (PP, 'Passport'),
        (ID, 'Identity Card'),
        (OT, 'Others')
    ]
    dtype = models.CharField(choices=DOC_TYPES, max_length=2)
    doc_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    
    def __str(self): 
        return self.doc_number