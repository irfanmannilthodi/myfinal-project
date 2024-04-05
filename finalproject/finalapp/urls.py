from . import views
from django.urls import path
app_name='finalapp'
urlpatterns = [
    path('',views.register,name='register'),
    path('login.',views.login,name='login'),
    path('irfanweb/',views.irfanweb,name='irfanweb'),
    path('marvel/<int:marvel_id>/',views.detail,name='detail'),
    path('irfanwebs',views.irfanwebs,name='irfanwebs'),
    path('dc/<int:dc_id>/',views.detail1,name='detail1'),
    path('irfanwebss',views.irfanwebss,name='irfanwebss'),
    path('monster/<int:monster_id>/',views.detail2,name='detail2'),
    path('add/',views.add,name='add'),
    path('add1/',views.add1,name='add1'),
    path('add2/',views.add2,name='add2'),
    path('update1/<int:id>/', views.update1, name='update1'),
    path('update2/<int:id>/',views.update2,name='update2'),
    path('update3/<int:id>/',views.update3,name='update3'),
    path('delete1/<int:id>/',views.delete1,name='delete1'),
    path('delete2/<int:id>/',views.delete2,name='delete2'),
    path('delete3/<int:id>/',views.delete3,name='delete3'),
    path('logout',views.logout,name='logout')




    ]


