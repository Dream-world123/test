from django.shortcuts import render
from .models import Designation_Detail, Franchise_Detail, Staff_Detail, Incentive_Detail, Payment_Detail
from django.contrib.sessions.middleware import SessionMiddleware
# Create your views here.

def details(request):
    return render(request, "detail.html")

def incentivedetails(request):
    if request.method=="POST":
        staff_id = request.POST['staff_id']
        year = request.POST['year']
        previousyear = int(year)
        previousyear = previousyear-1
        queryset1 = Incentive_Detail.objects.filter(staff_id=staff_id,year=previousyear)
        queryset2 = Incentive_Detail.objects.filter(staff_id=staff_id,  year=year)
        queryset3 = Payment_Detail.objects.filter(staff_id=staff_id,  year=year)
        queryset4 = Payment_Detail.objects.filter(staff_id=staff_id,  year=previousyear)
        queryset5 = Staff_Detail.objects.filter(id=staff_id)
        if queryset5:
            for i in queryset5:
                queryset6 = Franchise_Detail.objects.filter(id=i.franchise_code)
            if queryset6:
                for i in queryset6:
                    franchise = i.franchise_name
        if queryset5:
            for i in queryset5:
                queryset7 = Staff_Detail.objects.filter(id=i.introducer_id)
            if queryset7:
                for i in queryset7:
                    introducer = i.staff_name
        if queryset5:
            for i in queryset5:
                queryset8 = Designation_Detail.objects.filter(staff_id=i.id)
            if queryset8:
                for i in queryset8:
                    designation = i.designation
        totaldirect=0
        if queryset2:
            for i in queryset2:
                totaldirect=totaldirect+i.self_point
        totalteam=0
        if queryset2:
            for i in queryset2:
                totalteam=totalteam+i.team_point
        totalequal=0
        if queryset2:
            for i in queryset2:
                totalequal=totalequal+i.equal_share
        totaltravel=0
        if queryset2:
            for i in queryset2:
                totaltravel=totaltravel+i.travel_fund
        totalcar=0
        if queryset2:
            for i in queryset2:
                totalcar=totalcar+i.car_fund
        totalhome=0
        if queryset2:
            for i in queryset2:
                totalhome=totalhome+i.home_fund
        total=0
        if queryset2:
            for i in queryset2:
                total=total+i.total_incentive
        totalwelfare = 0
        if queryset2:
            for i in queryset2:
                totalwelfare=totalwelfare+i.welfare
        totaltds = 0
        if queryset2:
            for i in queryset2:
                totaltds=totaltds+i.tds
        previousamount=0
        if queryset1:
            for i in queryset1:
                previousamount=previousamount+i.net_incentive_payable
        totalamount=0
        if queryset2:
            for i in queryset2:
                totalamount=totalamount+i.net_incentive_payable
        previouspayment=0
        if queryset4:
            for i in queryset4:
                previouspayment=previouspayment+i.amount
        totalpayment=0
        if queryset3:
            for i in queryset3:
                totalpayment=totalpayment+i.amount
        balance = totalamount-totalpayment
        previousbalance = previousamount-previouspayment
        totalbalance = previousbalance+balance
        context = {
            'staff_data':queryset5,
            'year':year,
            'franchise':franchise,
            'introducer':introducer,
            'designation':designation,
            'data': queryset2,
            'datas': queryset3,
            'totaldirect':totaldirect,
            'totalteam':totalteam,
            'totalequal':totalequal,
            'totaltravel':totaltravel,
            'totalcar':totalcar,
            'totalhome':totalhome,
            'totalincentive': total,
            'totalwelfare' : totalwelfare,
            'totaltds' : totaltds,
            'totalamount' : totalamount,
            'totalpayment' : totalpayment,
            'openingbalance' : previousbalance,
            'totalbalance' : totalbalance
        }
    return render(request, "incentive_detail.html",context)



