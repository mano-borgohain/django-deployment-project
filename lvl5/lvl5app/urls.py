from django.conf.urls import url
from django.urls import path
from lvl5app import views

urlpatterns = [
    path('',views.index,name='lvl5app-index'),
    path('register/',views.register,name='lvl5app-registration'),
    path('login/',views.user_login,name='lvl5app-login'),
    path('logout/',views.user_logout,name='lvl5app-logout'),
]
