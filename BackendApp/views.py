from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from BackendApp.models import fooditemDB,number_basis_foodDB,number_basis_calorieDB,nutrientsDB
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'indexpage.html')
def login_page(request):
    return render(request,'login_page.html')
def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(index)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)
def add_fooditem(request):
    return render(request,'add_fooditem.html')
def save_fooditem(request):
    if request.method=="POST":
        food_name=request.POST.get('food_name')
        food_calorie = request.POST.get('food_calorie')
        food_image=request.FILES['food_image']
        obj=fooditemDB(food_name=food_name,food_calorie=food_calorie,food_image=food_image)
        obj.save()
        messages.success(request,'item added successfully')
        return redirect(add_fooditem)
def view_fooditem(request):
    data=fooditemDB.objects.all()
    return render(request,'view_fooditem.html',{'data':data})
def delete_fooditem(request,foodid):
    x=fooditemDB.objects.get(id=foodid)
    x.delete()
    messages.success(request, 'item removed successfully')
    return redirect(view_fooditem)
def add_numberbasis_items(request):
    return render(request,'add_numberbasis_items.html')

def save_numberbasis_item(request):
    if request.method=="POST":
        item_name=request.POST.get('item_name')
        obj=number_basis_foodDB(item_name=item_name)
        obj.save()
        messages.success(request,'item added successfully')
        return redirect(add_numberbasis_items)
def view_numberbasis_item(request):
    data=number_basis_foodDB.objects.all()
    return render(request,'view_numberbasis_items.html', {'data': data})
def add_numberbasis_item_calorie(request):
    data=number_basis_foodDB.objects.all()
    return render(request,'add_numberbasis_item_calorie.html', {'data': data})
def save_number_item_calorie(request):
    if request.method=="POST":
        item=request.POST.get('item')
        small = request.POST.get('small')
        medium = request.POST.get('medium')
        large = request.POST.get('large')
        item_image=request.FILES['item_image']
        obj=number_basis_calorieDB(item=item,small=small,medium=medium,large=large,item_image=item_image)
        obj.save()
        messages.success(request,'item added successfully')
        return redirect(add_numberbasis_item_calorie)
def add_nutrients(request):
    return render(request,'add_nutrients.html')
def save_nutrients(request):
    if request.method=="POST":
        name=request.POST.get('name')
        calorie = request.POST.get('calorie')
        carbohydrates = request.POST.get('carbohydrates')
        fiber = request.POST.get('fiber')
        protein = request.POST.get('protein')
        fat = request.POST.get('fat')
        image=request.FILES['image']
        obj=nutrientsDB(name=name,calorie=calorie,carbohydrates=carbohydrates,fiber=fiber,protein=protein,fat=fat,image=image)
        obj.save()
        messages.success(request,'item added successfully')
        return redirect(add_nutrients)

