# auth_project/auth_app/views.py

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib import messages
from django.contrib.auth.decorators import login_required # <--- NEW: Import login_required decorator
from .forms import UserRegistrationForm, CustomPasswordChangeForm


def register(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth_app/register.html', {'form': form})

def user_login(request):
    """Handles user login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'auth_app/login.html', {'form': form})

@login_required
def dashboard(request, section=None):
    """Displays the user's dashboard or a specific section (Help, About, Change Password)."""
    password_change_form = None
    if request.user.is_authenticated:
        password_change_form = CustomPasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if section == 'change_password':
            form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('dashboard_section', section='change_password')
            else:
                messages.error(request, 'Please correct the error below.')
                password_change_form = form

    context = {
        'user': request.user,
        'current_section': section if section else 'main',
        'password_change_form': password_change_form,
    }
    return render(request, 'auth_app/dashboard.html', context)

def user_logout(request):
    """Logs out the current user."""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

# --- NEW: Custom Password Reset Request View for Educational Purposes ---
def custom_password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # If user exists, generate the token and uid, then redirect directly
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            # Redirect directly to the password reset confirm page
            # This is the INSECURE part for educational demo
            messages.success(request, 'Email found! Redirecting to password reset page.')
            return redirect('password_reset_confirm', uidb64=uid, token=token)

        except User.DoesNotExist:
            # If email does not exist, show an error message
            messages.error(request, 'No user is registered with that email address.')
            # Stay on the same password reset form page
            return render(request, 'auth_app/password_reset_form.html')
    else:
        # For GET request, just display the form
        return render(request, 'auth_app/password_reset_form.html')
