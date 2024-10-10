from django.urls import path
from FrontendApp import views
urlpatterns=[
    path('dailytracker/', views.dailytracker, name='dailytracker'),
    path('', views.login, name='login'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('signup',views.signup,name='signup'),
    path('signupsave',views.signupsave,name='signupsave'),
    path('search/',views.search,name='search'),
    path('showitem',views.showitem,name='showitem'),
    path('item_added_save',views.item_added_save,name='item_added_save'),
    path('indexpage',views.indexpage,name='indexpage'),
    path('delete/<int:itemid>/',views.deleteitem,name='delete'),
    path('add_food/',views.add_food,name='add_food'),
    path('graph/',views.graph,name='graph'),
    path('save_final_data/',views.save_final_data,name='save_final_data'),
    path('BMI/',views.BMI,name='BMI')


]