from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

customer_types = (
    (1, "Customer"),
    (2, "Business"),
)

#Diesel, Petrol, Hybrid, Electric
FUEL_TYPES = (
    ("diesel", "Diesel"),
    ("petrol", "Petrol"),
    ("hybrid", "Hybrid"),
    ("electric", "Electric"),
)


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


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def is_customer(self):
        return Customer.objects.filter(user=self).exists()

    def is_business_owner(self):
        return Business.objects.filter(user=self).exists()


class Customer(models.Model):
    user = models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE)
    Location = models.CharField(max_length=50, choices=Locations.Malta_Locations, blank=False, null=False)
    Mobile = models.CharField(max_length=8, blank=False)
    Vat_Number = models.CharField(max_length=11, blank=True, null=True)
    ID_number = models.CharField(max_length=10, blank=False, unique=True)
    Address = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.user.email


class Car(models.Model):
    owner = models.ForeignKey(Customer, related_name="cars", on_delete=models.CASCADE)
    Brand = models.CharField(max_length=200)
    Model = models.CharField(max_length=200, blank=False)
    Fuel_Type = models.CharField(blank=False, choices=FUEL_TYPES, default="diesel", max_length=20)
    VIN = models.CharField(max_length=200, blank=False)
    NumPlate = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.NumPlate


class Business(models.Model):
    user = models.OneToOneField(User, related_name="business", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False)
    Location = models.CharField(max_length=50, choices=Locations.Malta_Locations, blank=False, null=False)
    Mobile = models.CharField(max_length=8, blank=False)
    Vat_Number = models.CharField(max_length=11, unique=True)
    Address = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    provider = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="services")

    def __str__(self):
        return self.name


class BookService(models.Model):
    client = models.ForeignKey(Customer, related_name="bookings", on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name="bookings", on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name="bookings", on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    deliver_date = models.DateField()
    acceptation = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["completed"]

    def __str__(self):
        return self.service.name
