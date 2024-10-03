from django.urls import path
from BackendApp import views


urlpatterns=[
    path('index/',views.index,name='index'),
    path('login_page/',views.login_page,name='login_page'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('add_fooditem/',views.add_fooditem,name='add_fooditem'),
    path('save_fooditem/',views.save_fooditem,name='save_fooditem'),
    path('view_fooditem/',views.view_fooditem,name='view_fooditem'),
    path('add_numberbasis_items/',views.add_numberbasis_items,name='add_numberbasis_items'),
    path('save_numberbasis_item/',views.save_numberbasis_item,name='save_numberbasis_item'),
    path('view_numberbasis_item/',views.view_numberbasis_item,name='view_numberbasis_item'),
    path('add_numberbasis_item_calorie/',views.add_numberbasis_item_calorie,name='add_numberbasis_item_calorie'),
    path('save_number_item_calorie/',views.save_number_item_calorie,name='save_number_item_calorie'),
    path('delete_fooditem/<int:foodid>/',views.delete_fooditem,name='delete_fooditem'),
    path('add_nutrients/',views.add_nutrients,name='add_nutrients'),
    path('save_nutrients/',views.save_nutrients,name='save_nutrients'),
]