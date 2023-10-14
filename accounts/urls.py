from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='homepage'),
    path('singup/' , views.singup , name='singuppage'),
    path('login/' , views.my_login , name='loginpage'),
    path('logout/',views.my_logout , name='logoutpage'),
    path('store/' , views.bookstore , name='storepage'),
    path('show/' , views.bookshow , name='showpage'),
    path('borrow/<int:id>' , views.borrowbook , name = 'borrowpage'),
    path('return/<int:id>' , views.returnbook , name='returnpage'),
]