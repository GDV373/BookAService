from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Locations(models.Model):
    Malta_Locations = [
        ('Attard', 'Attard'),
        ('Ħal-Balzan', 'Ħal-Balzan'),
        ('Il-Bidnija', 'Il-Bidnija'),
        ('Il-Birgu', 'Il-Birgu'),
        ('Birkirkara', 'Birkirkara'),
        ('Birżebbuġa', 'Birżebbuġa'),
        ('Bormla', 'Bormla'),
        ('Ħad-Dingli', 'Ħad-Dingli'),
        ('Il-Fgura', 'Il-Fgura'),
        ('Il-Furjana', 'Il-Furjana'),
        ('Ħal Għargħur', 'Ħal Għargħur'),
        ('Ħal Għaxaq', 'Ħal Għaxaq'),
        ('Il-Gudja', 'Il-Gudja'),
        ('Il-Gżira', 'Il-Gżira'),
        ('Il-Ħamrun', 'Il-Ħamrun'),
        ('L-Iklin', 'L-Iklin'),
        ('Il-Kalkara', 'Il-Kalkara'),
        ('Ħal Kirkop', 'Ħal Kirkop'),
        ('Ħal Lija', 'Ħal Lija'),
        ('Ħal Luqa', 'Ħal Luqa'),
        ('Il-Marsa', 'Il-Marsa'),
        ('Marsaskala', 'Marsaskala'),
        ('Marsaxlokk', 'Marsaxlokk'),
        ('L-Imdina', 'L-Imdina'),
        ('Il-Mellieħa', 'Il-Mellieħa'),
        ('L-Imġarr', 'L-Imġarr'),
        ('Il-Mosta', 'Il-Mosta'),
        ('L-Imqabba', 'L-Imqabba'),
        ('L-Imsida', 'L-Imsida'),
        ('L-Imtarfa', 'L-Imtarfa'),
        ('In-Naxxar', 'In-Naxxar'),
        ('Raħal Ġdid', 'Raħal Ġdid'),
        ('Pembroke', 'Pembroke'),
        ('Tal-Pietà', 'Tal-Pietà'),
        ('Ħal Qormi', 'Ħal Qormi'),
        ('Il-Qrendi', 'Il-Qrendi'),
        ('Ir-Rabat Malta', 'Ir-Rabat Malta'),
        ('Ħal Safi', 'Ħal Safi'),
        ('San Ġwann', 'San Ġwann'),
        ('Santa Luċija', 'Santa Luċija'),
        ('Santa Venera', 'Santa Venera'),
        ('L-Isla', 'L-Isla'),
        ('Is-Siġġiewi', 'Is-Siġġiewi'),
        ('Tas-Sliema', 'Tas-Sliema'),
        ('San Ġiljan', 'San Ġiljan'),
        ('San Pawl il-Baħar', 'San Pawl il-Baħar'),
        ('Is-Swieqi', 'Is-Swieqi'),
        ('Ħal Tarxien', 'Ħal Tarxien'),
        ('Ta Xbiex', 'Ta Xbiex'),
        ('Valletta', 'Valletta'),
        ('Ix-Xgħajra', 'Ix-Xgħajra'),
        ('Ħaż-Żabbar', 'Ħaż-Żabbar'),
        ('Ħaż-Żebbuġ', 'Ħaż-Żebbuġ'),
        ('Iż-Żejtun', 'Iż-Żejtun'),
        ('Iż-Żurrieq', 'Iż-Żurrieq'),
        ('Il-Fontana', 'Il-Fontana'),
        ('Għajnsiele', 'Għajnsiele'),
        ('L-Għarb', 'L-Għarb'),
        ('L-Għasri', 'L-Għasri'),
        ('Ta Kerċem', 'Ta Kerċem'),
        ('Il-Munxar', 'Il-Munxar'),
        ('Ix-Xlendi', 'Ix-Xlendi'),
        ('In-Nadur', 'In-Nadur'),
        ('Il-Qala', 'Il-Qala'),
        ('Ir-Raba', 'Ir-Raba'),
        ('San Lawrenz', 'San Lawrenz'),
        ('Ta Sannat', 'Ta Sannat'),
        ('Ix-Xagħra', 'Ix-Xagħra'),
        ('Ix-Xewkija', 'Ix-Xewkija'),
        ('Iż-Żebbuġ Gozo', 'Iż-Żebbuġ Gozo'),
        ('Marsalforn', 'Marsalforn'),
    ]
 


class Car(models.Model):
    Brand = models.CharField(max_length=200)
    Model = models.CharField(max_length=200, blank=False)
    Fuel_Type =  models.IntegerField(blank=False)
    VIN = models.CharField(max_length=200, blank=False)
    NumPlate = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.NumPlate

class Customer(models.Model):
    Name = models.CharField(max_length=200)
    Location = models.CharField(max_length=50, choices = Locations.Malta_Locations, blank =False, null =False)
    Mobile = models.CharField(max_length=8, blank=False)
    Vat_Number =  models.CharField(max_length=10, blank=True)
    ID_number = models.CharField(max_length=10, blank=False, unique=True)
    Email = models.EmailField(blank=False)
    Address = models.CharField(max_length=200, blank=False)
    Service = models.CharField(max_length=200, blank=False)
    carFK = models.ForeignKey(Car, on_delete=models.PROTECT)

    def __str__(self):
        return self.Name


class BusinessCustomer(models.Model):
    Owner_Name = models.CharField(max_length=200, blank=False)
    Business_Name = models.CharField(max_length=200, blank=False)
    Location = models.CharField(max_length=50, choices = Locations.Malta_Locations, blank =False, null =False)
    Mobile = models.CharField(max_length=8, blank=False)
    Vat_Number =   models.CharField(max_length=10, blank=False, unique=True)
    Email = models.EmailField(blank=False)
    Address = models.CharField(max_length=200, blank=False)
    Service = models.CharField(max_length=200, blank=False)
    carFK = models.ForeignKey(Car, on_delete=models.PROTECT)
    customerFK = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return self.Business_Name