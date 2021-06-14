from django.contrib import admin
from django.contrib.auth.models import Group
#from django.contrib.admin.models import LogEntry
from import_export.admin import ImportExportModelAdmin
from .models import Staff_Detail, Incentive_Detail, Payment_Detail, Address_Detail,Franchise_Detail,Designation_Detail,Nominee_Detail
# Register your models here.

class ViewAdmin(ImportExportModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Address Details",{
            "fields": (
                ('id'),('taluk'),('district'),('state'),('country')    
            )
        }
        ),
    )

    list_display = ('id','taluk','district','state','country','created')
    list_filter = ('created',)
    search_fields = ('id','taluk','district','state','country')
    list_per_page = 30


class FranchiseAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Franchise Details",{
            "fields": (
                ('id'),('franchise_name')    
            )
        }
        ),
    )

    list_display = ('id','franchise_name','created')
    list_filter = ('created',)
    search_fields = ('id','franchise_name')
    list_per_page = 30


class DesignationAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Designation Details",{
            "fields": (
                ('staff_id'),('designation')    
            )
        }
        ),
    )

    list_display = ('staff_id','designation','created')
    list_filter = ('created',)
    search_fields = ('staff_id','designation')
    list_per_page = 30

class StaffAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Personal Details",{
            "fields": (
                ('id','staff_name'),('gender','father_name'),('date_of_birth','image')    
            )
        }

        ),
        ("Address Details",{
            "fields": (
                ('address'),('village','pincode')
            )
        }
        ),
        ("Contact Details",{
            "fields": (
                ('mobile_no','email'),
            )
        }
        ),
        ("Identification Details",{
            "fields": (
                ('pancard','pan_img'),('adhar','adhar_img')
            )
        }
        ),
        ("Bank Account Details",{
            "fields": (
                ('account_holder','bank_name'),('branch_name','account_type'),('account_number','ifsc_code'),('bank_img')   
            )
        }
        ),
        ("Franchise Details",{
            "fields": (
                ('franchise_code'),
            )
        }
        ),
        ("Introducer Details",{
            "fields": (
                ('introducer_id'),
            )
        }
        ),
    )

    list_display = ('id','staff_name','gender','father_name','date_of_birth','image','address','village','pincode','mobile_no','email','pancard','pan_img','adhar','adhar_img','account_holder','bank_name','branch_name','account_type','account_number','ifsc_code','bank_img','franchise_code','introducer_id','created')
    list_filter = ('created',)
    search_fields = ('id','staff_name')
    list_per_page = 30

class NomineeAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Staff Details",{
            "fields": (
                ('staff_id'), 
            )
        }
        ),
        ("Nominee Details",{
            "fields": (
                ('nominee','date_of_birth'),('relationship')   
            )
        }
        ),
        ("Address Details",{
            "fields": (
                ('address'),('village','pincode')
            )
        }
        ),
        ("Contact Details",{
            "fields": (
                ('mobile_no'),
            )
        }
        ),
    )

    list_display = ('staff_id','nominee','date_of_birth','relationship','address','village','pincode','mobile_no','created')
    list_filter = ('created',)
    search_fields = ('staff_id','nominee')
    list_per_page = 30


class IncentiveAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Staff Details",{
            "fields": (
                ('staff_id'),
            )
        }
        ),
        ("Duration",{
            "fields": (
                ('month','year'),   
            )
        }

        ),
        ("Purchase Details",{
            "fields": (
                ('self_purchase','purchase_amount'),
            )
        }
        ),
        ("Weightage Details",{
            "fields": (
                ('self_weightage','team_weightage'),('net_weightage')
            )
        }
        ),
        ("Points Details",{
            "fields": (
                ('self_point','team_point'),('net_points')
            )
        }
        ),
        ("Equal Share Details",{
            "fields": (
                ('equal_share'),
            )
        }
        ),
        ("Travel Fund Details",{
            "fields": (
                ('travel_fund'),
            )
        }
        ),
        ("Car Fund Details",{
            "fields": (
                ('car_fund'),
            )
        }
        ),
        ("Home Fund Details",{
            "fields": (
                ('home_fund'),
            )
        }
        ),
        ("Total Incentive Details",{
            "fields": (
                ('total_incentive'),
            )
        }
        ),
        (" Welfare & TDS Details",{
            "fields": (
                ('welfare','tds'),
            )
        }
        ),
        ("Payable Amount Details",{
            "fields": (
                ('net_incentive_payable'),
            )
        }
        ),
    )

    list_display = ('staff_id','month','year','self_purchase','purchase_amount','self_weightage','team_weightage','net_weightage','self_point','team_point','net_points','equal_share','travel_fund','car_fund','home_fund','total_incentive','welfare','tds','net_incentive_payable','created')
    list_filter = ('created',)
    search_fields = ('Staff_id','month','year')
    list_per_page = 30


class PaymentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Staff Details",{
            "fields": (
                ('staff_id'), 
            )
        }
        ),
        ("Duration",{
            "fields": (
                ('month','year'),   
            )
        }
        ),
        ("Payment Details",{
            "fields": (
                ('date','account_number'),('ifsc_code','amount')
            )
        }
        ),
    )

    list_display = ('staff_id','month','year','date','account_number','ifsc_code','amount','created')
    list_filter = ('created',)
    search_fields = ('staff_id','month','year')
    list_per_page = 30


class AddressView(ViewAdmin, AddressAdmin):
    pass

class FranchiseView(ViewAdmin, FranchiseAdmin):
    pass

class DesignationView(ViewAdmin, DesignationAdmin):
    pass

class NomineeView(ViewAdmin, NomineeAdmin):
    pass

class StaffView(ViewAdmin, StaffAdmin):
    pass

class IncentiveView(ViewAdmin,IncentiveAdmin):
    pass

class PaymentView(ViewAdmin,PaymentAdmin):
    pass



admin.site.unregister(Group)
#LogEntry.objects.all().delete()
admin.site.register(Address_Detail,AddressView)
admin.site.register(Franchise_Detail,FranchiseView)
admin.site.register(Designation_Detail,DesignationView)
admin.site.register(Nominee_Detail,NomineeView)
admin.site.register(Staff_Detail,StaffView)
admin.site.register(Incentive_Detail,IncentiveView)
admin.site.register(Payment_Detail,PaymentView)


