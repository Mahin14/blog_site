from django.urls import path
from App_login import views
app_name='App_login'
urlpatterns = [
    path('sign_up/',views.sign_up,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('update_profile/',views.user_change,name='ChangeProfile'),
    path('password/',views.pass_change,name='ChangePass'),
    path('add_picture/',views.add_pro_pic,name='AddPicture'),
    path('change_picture/',views.change_pro_pic,name='ChangePicture'),







]
