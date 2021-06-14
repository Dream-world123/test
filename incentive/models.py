from django.db import models
from django.db.models.deletion import CASCADE
from gst_field.modelfields import GSTField, PANField
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from pkg_resources import require

# Create your models here.

class Address_Detail(models.Model):
    id = models.CharField(primary_key=True, null=False, verbose_name=("Pin Code"),max_length=6)
    taluk = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'address_detail'
        verbose_name = 'Address Detail'


class Franchise_Detail(models.Model):
    id = models.CharField(primary_key=True, null=False, verbose_name=("Franchise Code"),max_length=30)
    franchise_name = models.CharField(verbose_name=("Franchise Name"),max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'franchise_detail'
        verbose_name = 'Franchise Detail'


class Staff_Detail(models.Model):
    id = models.CharField(max_length=30 , primary_key=True , null=False, verbose_name=("Staff ID"))
    staff_name = models.CharField(verbose_name=("Staff Name"),max_length=30)
    GENDER_SELECT = (
        ('0', 'Female'),
        ('1', 'male'),
    )
    gender = models.CharField(max_length=11,choices=GENDER_SELECT)
    father_name = models.CharField(verbose_name=("Father/Husband"),max_length=30)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to = 'images/')
    address = models.TextField()
    village = models.CharField(max_length=30)
    pincode = models.ForeignKey(Address_Detail, on_delete=CASCADE, verbose_name=("Pin Code"))
    mobile_regex = RegexValidator(regex=r'^[0-9]{10}$', code='Invalid')
    mobile_no = models.CharField(verbose_name=("Mobile Number"),max_length=10, validators=[mobile_regex])
    email = models.EmailField(max_length = 50)
    pancard = PANField()
    pan_img = models.ImageField(verbose_name=("Pancard Image"),upload_to = 'images/')
    adhar_regex = RegexValidator(regex=r'^[0-9]{12}$', code='Invalid')
    adhar = models.CharField(verbose_name=("Adhar Card"),max_length=12, validators=[adhar_regex])
    adhar_img = models.ImageField(verbose_name=("Adhar_card Image"),upload_to = 'images/')
    account_holder = models.CharField(verbose_name=("Account Holder Name"),max_length=20)
    bank_name = models.CharField(verbose_name=("Bank Name"),max_length=20)
    branch_name = models.CharField(verbose_name=("Branch Name"),max_length=20)
    account_type = models.CharField(verbose_name=("Account Type"),max_length=20)
    account_regex = RegexValidator(regex=r'^[0-9]*$', code='Invalid')
    account_number = models.CharField(verbose_name=("Account Number"),max_length=20, validators=[account_regex])
    ifsc_regex = RegexValidator(regex=r'^[A-Z]{4}0[A-Z0-9]{6}$', code='Invalid')
    ifsc_code = models.CharField(verbose_name=("IFSC Code"),max_length=11, validators=[ifsc_regex])
    bank_img = models.ImageField(verbose_name=("Bank Image"),upload_to = 'images/')
    franchise_code = models.ForeignKey(Franchise_Detail, on_delete=models.CASCADE,verbose_name=("Franchise Code"))
    introducer_id = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name=("Introducer Id"), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id

    class Meta:
        db_table = 'staff_detail'
        verbose_name = 'Staff Detail'


class Designation_Detail(models.Model):
    staff_id = models.ForeignKey(Staff_Detail, on_delete=CASCADE, verbose_name=("Staff ID")) 
    DESIGNATION_SELECT=(  

        ('Marketing Exicutive(ME)','Marketing Exicutive(ME)'),
        ('SR.Marketing Exicutive(SR.ME)','SR.Marketing Exicutive(SR.ME)'),
        ('Marketing Organizer(MO)','Marketing Organizer(MO)'),
        ('SR.Marketing Organizer(SR.MO)','SR.Marketing Organizer(SR.MO)'),
        ('Marketing Manager(MM)','Marketing Manager(MM)'),
        ('SR.Marketing Manager(SR.MM)','SR.Marketing Manager(SR.MM)'),
        ('Marketing Regional Manager(MRM)','Marketing Regional Manager(MRM)'),
        ('SR.Marketing Regional Manager(SR.MRM)','SR.Marketing Regional Manager(SR.MRM)'),
        ('Marketing Zonal Manager(MZM)','Marketing Zonal Manager(MZM)'),
        ('SR.Marketing Zonal Manager(SR.MZM)','SR.Marketing Zonal Manager(SR.MZM)'),
        ('Marketing Advisor(MA)','Marketing Advisor(MA)'),
        ('SR.Marketing Advisor(SR.MA)','SR.Marketing Advisor(SR.MA)'),
        ('SR.Marketing Advisor Group(SR.MAG)','SR.Marketing Advisor Group(SR.MAG)'),
        ('Director','Director'),
    )
    designation = models.CharField(max_length=40, choices=DESIGNATION_SELECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.staff_id)

    class Meta:
        db_table = 'designation_detail'
        verbose_name = 'Designation Detail'


class Nominee_Detail(models.Model):
    staff_id = models.ForeignKey(Staff_Detail, on_delete=models.CASCADE, verbose_name=("Staff ID"))
    nominee = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    relationship = models.CharField(max_length=30)
    address = models.TextField()
    village = models.CharField(max_length=30)
    pincode = models.ForeignKey(Address_Detail, on_delete=CASCADE, verbose_name=("Pin Code"))
    mobile_regex = RegexValidator(regex=r'^[0-9]{10}$', code='Invalid')
    mobile_no = models.CharField(verbose_name=("Mobile Number"),max_length=10, validators=[mobile_regex])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.staff_id)

    class Meta:
        db_table = 'nominee_detail'
        verbose_name = 'Nominee Detail'

class Incentive_Detail(models.Model):
    staff_id = models.ForeignKey(Staff_Detail, on_delete=models.CASCADE, verbose_name=("Staff ID"))
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    self_purchase = models.FloatField(verbose_name=("Self Purchase"), default=0.0)
    purchase_amount = models.FloatField(verbose_name=("Purchase Amount"), default=0.0)
    self_weightage = models.FloatField(verbose_name=("Self Weightage"), default=0.0)
    team_weightage = models.FloatField(verbose_name=("Team Weightage"), default=0.0)
    net_weightage = models.FloatField(verbose_name=("Net Weightage"), default=0.0) 
    self_point = models.FloatField(verbose_name=("Self Point"), default=0.0)
    team_point = models.FloatField(verbose_name=("Team Point"), default=0.0)
    net_points = models.FloatField(verbose_name=("Net Points"), default=0.0)
    equal_share = models.FloatField(verbose_name=("Equal Share"), default=0.0)
    travel_fund = models.FloatField(verbose_name=("Travel Fund"), default=0.0)
    car_fund = models.FloatField(verbose_name=("Car Fund"), default=0.0)
    home_fund = models.FloatField(verbose_name=("Home Fund"), default=0.0)
    total_incentive = models.FloatField(verbose_name=("Total Incentive"), default=0.0)
    welfare = models.FloatField(verbose_name=("Welfare 1%"),default=0.0)
    tds = models.FloatField(verbose_name=("TDS 5%"), default=0.0)
    net_incentive_payable = models.FloatField(verbose_name=("Net Incentive Payable"), default=0.0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.staff_id)

    class Meta:
        db_table = 'incentive_detail'
        verbose_name = 'Incentive Detail'

class Payment_Detail(models.Model):
    staff_id = models.ForeignKey(Staff_Detail, on_delete=models.CASCADE, verbose_name=("Staff ID"))
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    date = models.DateField()
    account_regex = RegexValidator(regex=r'^[0-9]*$', code='Invalid')
    account_number = models.CharField(verbose_name=("Account Number"),max_length=20, validators=[account_regex])
    ifsc_regex = RegexValidator(regex=r'^[A-Z]{4}0[A-Z0-9]{6}$', code='Invalid')
    ifsc_code = models.CharField(verbose_name=("IFSC Code"),max_length=11, validators=[ifsc_regex])
    amount = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.staff_id)

    class Meta:
        db_table = 'payment_detail'
        verbose_name = 'Payment Detail'


