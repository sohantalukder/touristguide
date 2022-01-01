from django.urls import path
from .views import *
# ----------- import for Login,Logout authentication and render template ----------------- #
from django.contrib.auth import views as auth_views
from .form import *

urlpatterns = [
    path('registration/', registrationView, name='registration'),
    path('signin/', loginView, name='signin'),
    path('logout/', logoutView.as_view(), name='logout'),
    # # password setup url
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='account/passwordchange.html',form_class=AccountPasswordchangeForm,success_url='/account/passwordchangedone/'),name='passwordchange'),

    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='account/passwordchangedone.html'),name='passwordchangedone'),

    # # ----------- for password reset url ----------------- #

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='account/password_reset.html',form_class=AccountPasswordResetForm), name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',form_class=AccountsetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),
]