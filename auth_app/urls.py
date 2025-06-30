# auth_project/auth_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views # Keep for password reset confirm/complete views
from . import views # Your custom views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:section>/', views.dashboard, name='dashboard_section'),

    # NEW: Point password_reset to your custom view
    path('password_reset/', views.custom_password_reset_request, name='password_reset'),

    # Keep Django's default views for confirm and complete as they handle the backend logic
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='auth_app/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='auth_app/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='auth_app/password_reset_complete.html'),
         name='password_reset_complete'),

    path('', views.user_login, name='home'),
    
]
