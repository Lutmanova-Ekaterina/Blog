from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import *


app_name = UsersConfig.name

urlpatterns = [
    path('', SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignupView.as_view(), name='register'),
    path('register/success/', SignupSuccessView.as_view(), name='register_success'),
    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/<uidb64>/confirm/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/done/',
         CustomPasswordResetDoneView.as_view(template_name='users/reset_confirm.html'), name='password_reset_done'),
    path('password/reset/complete/', CustomPasswordResetCompleteView.as_view(template_name='users/password_reset_form.html'),
         name='password_reset_complete'),
    path('verify/<str:token>/', verify_email, name='verify_email'),
    path('simple/reset/', simple_reset_password, name='simple_reset'),
    path('user_list/', UsersListView.as_view(), name='user_list'),
    path('user_change/<int:pk>/', user_status_change, name='user_change')
]
