from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import Template
from django.template import loader
from django.http import HttpResponse
import math


class DEPView(TemplateView):
    template_name = 'DepreciationCalculator.html'

# class DDBView(TemplateView):
#     template_name = 'DDB.html'
    
class Footer7View(TemplateView):
    template_name = 'Footer7.html'






def doubledb(request):
    c = {   'tit' : 'Double Declining Balance Depreciation Calculator'}
    temp = loader.get_template('DDB.html')
    return HttpResponse(temp.render(c, request))

def syd(request):
    c = {   'tit' : 'Sum of the Years Digits Depreciation Calculator'}
    temp = loader.get_template('DDB.html')
    return HttpResponse(temp.render(c, request))


def straightline(request):
    c = {   'tit' : 'Straight Line Depreciation Calculator'}
    temp = loader.get_template('DDB.html')
    return HttpResponse(temp.render(c, request))    


def calculate(request):
    if request.method == 'POST':
        bal = request.POST.get('cst')
        yrs = request.POST.get('lif')
        salv = request.POST.get('sal')  
        balance = int(bal)
        years = int(yrs) 
        salvage = int(salv)       
        typ = request.POST.get('typ')  
    if typ == "Double Declining Balance Depreciation Calculator":
        dict= {}
        dict = doubl(years, balance, salvage, typ)
        temp = loader.get_template('DDBOutput.html')
        return HttpResponse(temp.render(dict, request))
    if typ == "Sum of the Years Digits Depreciation Calculator":
        dict= {}
        dict = suyrdt(years, balance, salvage, typ)
        temp = loader.get_template('DDBOutput.html')
        return HttpResponse(temp.render(dict, request))
    if typ == "Straight Line Depreciation Calculator":
        dict= {}
        dict = straightL(years, balance, salvage, typ)
        temp = loader.get_template('DDBOutput.html')
        return HttpResponse(temp.render(dict, request))



def doubl(years, balance, salvage, typ):
    YEARS = years
    dog = 0
    ar = []
    br = []
    cr = []
    ar.append('0')
    cr.append('NONE')
    rate = (1/years) * 2
    result = depreciatingRate(balance, rate, salvage, years, dog, ar, br, cr)
   

    c = {   'tit' : "Double Declining Balance",
            'bal' : 'Balance',
            'dep' : 'Depreciation',
            'ar' : ar,
            'br' : br,
            'cr' : cr,
            'balance': balance,
            'years' : years,
            'salvage' : salvage,
            'color' : '#d1e8e1'
        }
    return c  
    
def depreciatingRate(BALANCE, RATE, SALVAGE, YEARS, dog, ar, br, cr):
        dog = dog + 1
        YEARS = YEARS - 1
        if YEARS == 0 : 
            ar.append(math. floor((dog))), br.append(math. floor((BALANCE)))  , cr.append(math.floor(BALANCE - SALVAGE))
            
        if YEARS == 0:
            # ar.append(0), br.append(math. floor((SALVAGE))), cr.append(0)
            br.append(math. floor((SALVAGE)))
            return
        if BALANCE - SALVAGE -(BALANCE -(BALANCE - BALANCE* RATE)) > 0.00:
            ar.append(math. floor((dog))), br.append(math. floor((BALANCE)))  ,cr.append(math.floor((BALANCE -(BALANCE - BALANCE* RATE))))
            return YEARS > 0 and depreciatingRate(BALANCE - (RATE * BALANCE), RATE, SALVAGE, YEARS, dog, ar, br, cr)
        else: 
            ar.append(math. floor((dog))), br.append(math. floor((BALANCE))), cr.append(math.floor(BALANCE - SALVAGE))
            ar.append(0), br.append(math. floor((SALVAGE))), cr.append(0)
        
            
def suyrdt(years, balance, salvage, typ):
    
    z =[]    
    e = 0    
    for a in range(1, years + 1):
        e = e + a            
    syd = e
    base = balance - salvage
    rate = years/syd
    depr = 0
    bal = balance

    ar = []
    br = []
    cr = []
    ar.append('0')
    cr.append('NONE')
    br.append(balance)
    result = sumYD(base, years, syd, bal, z, ar, br, cr)

    h = {   'tit' : "Sum of the Years Digits",
            'bal' : 'Balance',
            'dep' : 'Depreciation',
            'res' : result,
            'ar' : ar,
            'br' : br,
            'cr' : cr, 
            'balance': balance,
            'years' : years,
            'salvage' : salvage,
            'color' : '#EEB983'        
        }

    return h        
    
def sumYD(b, y, syd, bal, z, ar, br, cr ):
    if y < 1: return b - bal
    z.append(y)
    rate = (y/syd)
    depr = b * rate
    bal = bal - depr 
    bal = round(bal, 0)
    depr = round(depr, 0)
    z.sort()
    ar.append(z[(len(z)-1)] - z[0]+ 1) 
    cr.append(int(depr))
    br.append(int(bal))    
    sumYD(b, y - 1, syd, bal, z, ar, br, cr)

   
def straightL(years, balance, salvage, typ):  
    e = 0    
    base = balance - salvage
    depr = base/years
    depr = round(depr, 0)
    ar = []
    br = []
    cr = []
    ar.append('0')
    cr.append('NONE')
    br.append(balance)
    result = SL(balance, years, e, depr, ar, br, cr)

    b = {   'tit' : "Straight Line",
            'bal' : 'Balance',
            'dep' : 'Depreciation',
            'res' : result,
            'ar' : ar,
            'br' : br,
            'cr' : cr, 
            'balance': balance,
            'years' : years,
            'salvage' : salvage,
            'color' : "#F7F4AF"         
        }

    return b


def SL(balance, years, e, depr, ar, br, cr):
    if years < 1: return balance
    e = e + 1
    balance = balance - depr
    years = years - 1
    ar.append(e)
    br.append(int(balance))
    cr.append(int(depr))
    SL(balance, years, e, depr, ar, br, cr)
    



        
    
    
    

      