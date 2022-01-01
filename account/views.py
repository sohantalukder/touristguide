from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .form import SignupForm,LoginForm
from django.contrib import messages
from django.views import View
# Create your views here.

def registrationView(request):
    if not request.user.is_authenticated:
        template_name = 'account/registration.html'
        context = {}
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account Create Successfully! Please Login.')
                user = form.save()
                login(request, user)
                return redirect('profile')
                # return redirect('signin')
            else:
                messages.success(request, 'Please enter your valid information.')
                form = SignupForm()
                context = {
                'forms': form
                }
        else:
            form = SignupForm()
            context = {
                'forms': form
                }
        return render(request, template_name , context)
    else:
        return redirect('profile')

def loginView(request):
    if not request.user.is_authenticated:
        nxt = request.GET.get("next", None)
        template_name = 'account/signin.html'
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if nxt is not None:
                        return redirect(request.GET.get("next"))
                    return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password',extra_tags="login")
            return redirect('signin')
        else:
            form = LoginForm()
            return render(request, template_name, {'form': form})
    else:
        return redirect('profile')


class logoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'Account logout Successfully')
            return redirect('home')
        else:
            return redirect('signin')

