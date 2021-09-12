from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import Template
from django.template import loader
from django.http import HttpResponse
import math

# Create your views here.
class DDBView(TemplateView):
    template_name = 'DDB.html'
    
class Footer7View(TemplateView):
    template_name = 'Footer7.html'

def calculate(request):
    if request.method == 'POST':

        bal = request.POST.get('cst')
        yrs = request.POST.get('lif')
        salv = request.POST.get('sal')  

        balance = int(bal)
        years = int(yrs) 
        salvage = int(salv)
#    print("")
#    print("DOUBLE DECLINING BALANCE")
#    print("")
#    print("%18s" "%20s" %("BALANCE", "DEPRECIATION"))
    
    dog = 0
    ar = []
    br = []
    cr = []
    rate = (1/years) * 2
    result = depreciatingRate(balance, rate, salvage, years, dog, ar, br, cr)
#    if result == False: salvo = salvage
#    for rat in ar:
#        print(rat)
#    for cat in br:
#        print(cat)
#    for bat in cr:
#        print(bat)
    # return result
    c = {   'tit' : 'Double Declining Balance',
            'bal' : 'Balance',
            'dep' : 'Depreciation',
            'res' : result,
            'ar' : ar,
            'br' : br,
            'cr' : cr,
            'balance': balance,
            'years' : years,
            'salvage' : salvage
        }            
    temp = loader.get_template('DDBOutput.html')
    return HttpResponse(temp.render(c, request))



    
def depreciatingRate(BALANCE, RATE, SALVAGE, YEARS, dog, ar, br, cr):
        dog = dog + 1
        YEARS = YEARS - 1
        if BALANCE - SALVAGE -(BALANCE -(BALANCE - BALANCE* RATE)) > 0.00:
            ar.append(math. floor((dog))), br.append(math. floor((BALANCE)))  ,cr.append(math.floor((BALANCE -(BALANCE - BALANCE* RATE))))
#           print("%-2d" "%16d" "%16d"  % (dog, BALANCE  ,BALANCE -(BALANCE - BALANCE* RATE)))
            
            return YEARS > -1 and depreciatingRate(BALANCE - (RATE * BALANCE), RATE, SALVAGE, YEARS, dog, ar, br, cr)
        else: 
#           print("%2d" "%16d" "%16d" % (dog, BALANCE,  min(BALANCE - SALVAGE, BALANCE -(BALANCE - BALANCE* RATE))))
            ar.append(math.floor((dog))), br.append(math.floor((BALANCE))),  cr.append(math.floor((min(BALANCE - SALVAGE, BALANCE -(BALANCE - BALANCE* RATE))))) 
#           print(SALVAGE)    


   


