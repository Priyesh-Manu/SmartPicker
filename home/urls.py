from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('multiSection/',views.multi,name='multiSelection'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
]
