
from django.urls import path,include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('special/', views.special, name='special'),
    path('user_login/',views.user_login,name='user_login'),
    path('register/', views.register,name = 'register'),

]
