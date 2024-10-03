from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from FrontendApp.models import signupDB,calorieDB,item_addedDB,final_dataDB
from BackendApp.models import fooditemDB,number_basis_foodDB,number_basis_calorieDB,nutrientsDB
from django.contrib import messages
from datetime import date

# 2c+UiUckPgyc0bZJWugAGg==zgXuv58x7HY7fXup

# Create your views here.


def dailytracker(request):
    today = str(date.today())
    datetoday=item_addedDB.objects.filter(datepicker=today)
    data=signupDB.objects.filter(username=request.session['username'])
    added = item_addedDB.objects.filter(username=request.session['username'])


    item=item_addedDB.objects.filter(username=request.session['username'])

    # date=datetime.datetime.now()

    total=0
    calorie=0


    for i in data:
        calorie = i.calorie_intake
    rem_calorie = calorie
    for i in added:
        if str(i.datepicker) == today:
            total += ((i.calorie_added)*(i.quantity))
            print(((i.calorie_added)*(i.quantity)))
            rem_calorie = calorie - total


        if rem_calorie<0:
            messages.warning(request,'Calorie intake exceeded ')
        if 'q' in request.GET:
            q = request.GET['q']
            nutrients = nutrientsDB.objects.filter(name__icontains=q)
        else:
            nutrients = nutrientsDB.objects.all()
    return render(request,'dailytracker.html',{'datetoday':datetoday,'item':item,'data':data,'date':date,'nutrients':nutrients,'rem_calorie':rem_calorie,'calorie':calorie,'total':total,'today':today})
def login(request):
    return render(request,'login.html')
def userlogin(req):
    if req.method=="POST":
        un=req.POST.get('username')
        pwd=req.POST.get('password')
        if signupDB.objects.filter(username__contains=un,password=pwd).exists():
            req.session['username'] = un
            req.session['password'] = pwd
            messages.success(req, 'Welcome!')
            return redirect(indexpage)
        else:
            messages.error(req, 'Invalid Credentials')
            return redirect(login)
    else:
        messages.error(req, 'User not found')
        return redirect(login)
def signup(request):
    return render(request,'signup.html')
def signupsave(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email = request.POST.get('email')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        password = request.POST.get('password1')
        if gender == 'male':
            calorie_intake = 66.47 + (13.75 * int(weight)) + (5.003 * int(height)) - (6.755 * int(age))
        else:
            calorie_intake = 655.1 + (9.563 * int(weight)) + (1.850 * int(height)) - (4.676 * int(age))

        obj=signupDB(username=username,email=email,height=height,weight=weight,age=age,gender=gender,password=password,calorie_intake=calorie_intake)
        obj.save()
        messages.success(request,'Registered Successfully.Now you can login')
        return redirect(signup)

def showitem(request):
    data = signupDB.objects.filter(username=request.session['username'])
    date = datetime.datetime.now()
    nutrients=nutrientsDB.objects.all()
    added=item_addedDB.objects.all()
    calorie=0
    rem_calorie=calorie
    for i in data:
        calorie=i.calorie_intake
    for i in added:
        rem_calorie=calorie-i.calorie_added

    return render(request,'show_item.html',{'data':data,'date':date,'nutrients':nutrients,'calorie':rem_calorie})
def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login)
def item_added_save(request):
     if request.method=="POST":
        item = item_addedDB.objects.filter(username=request.session['username'])
        hiddenusername=request.POST.get('hiddenusername')
        datepicker=request.POST.get('datepicker')
        name_added=request.POST.get('name_added')
        calorie_added=request.POST.get('calorie_added')
        calorie_intake=request.POST.get('calorie_intake')
        quantity=request.POST.get('quantity')
        total_calorie=request.POST.get('total_calorie')
        obj=item_addedDB(quantity=quantity,username=hiddenusername,name_added=name_added,calorie_added=calorie_added,datepicker=datepicker,calorie_intake=calorie_intake,total_calorie=total_calorie)
        obj.save()
        messages.success(request,'item added')
        return redirect(add_food)
def search(request):
    if 'q' in request.GET:
        q=request.GET['q']
        return nutrientsDB.objects.filter(name__icontains=q)

def indexpage(request):
    data = signupDB.objects.filter(username=request.session['username'])
    added = item_addedDB.objects.filter(username=request.session['username'])

    today = str(date.today())
    item = item_addedDB.objects.filter(username=request.session['username'])
    nutrients = nutrientsDB.objects.all()


    total = 0
    calorie = 0

    for i in data:
        calorie = i.calorie_intake
    rem_calorie = calorie
    for i in added:
        if str(i.datepicker) == today:
            total += ((i.calorie_added)*(i.quantity))
            rem_calorie = calorie - total

        if rem_calorie < 0:
            rem_calorie = 0
            messages.warning(request, 'Calorie intake exceeded ')


    return render(request, 'indexpage.html',
                  {'item': item, 'data': data, 'date': date, 'nutrients': nutrients, 'rem_calorie': rem_calorie,
                   'calorie': calorie, 'total': total, 'today': today})
def deleteitem(request,itemid):
    x=item_addedDB.objects.filter(id=itemid)
    x.delete()
    messages.success(request,'item deleted')
    return redirect(add_food)
def add_food(request):
    today = str(date.today())
    datetoday = item_addedDB.objects.filter(datepicker=today,username=request.session['username'])
    data = signupDB.objects.filter(username=request.session['username'])
    added = item_addedDB.objects.filter(username=request.session['username'])

    item = item_addedDB.objects.filter(username=request.session['username'])

    # date=datetime.datetime.now()

    total = 0
    calorie = 0

    for i in data:
        calorie = i.calorie_intake
    rem_calorie = calorie
    for i in added:
        if str(i.datepicker) == today:
            total += ((i.calorie_added) * (i.quantity))
            print(((i.calorie_added) * (i.quantity)))
            rem_calorie = calorie - total

        if rem_calorie < 0:
            rem_calorie = 0
            messages.warning(request, 'Calorie intake exceeded ')
    if 'q' in request.GET:
        q=request.GET['q']
        nutrients = nutrientsDB.objects.filter(name__icontains=q)
    else:
        nutrients = nutrientsDB.objects.all()
    return render(request,'add_food.html',{'datetoday':datetoday,'item':item,'data':data,'date':date,'nutrients':nutrients,'rem_calorie':rem_calorie,'calorie':calorie,'total':total,'today':today})
def graph(request):
    data = signupDB.objects.filter(username=request.session['username'])
    final=final_dataDB.objects.filter(username=request.session['username'])
    for i in final:
        print(i.day)
        print(i.total)
    context={
        'data':data,
        'final':final
    }
    return render(request,'graph.html',context)
def save_final_data(request):
    if request.method=="POST":
        username=request.POST.get('username')
        total=request.POST.get('total')
        day=request.POST.get('day')
        obj=final_dataDB(username=username,total=total,day=day)
        obj.save()
        return redirect(indexpage)
















