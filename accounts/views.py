import random
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import Profile


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('profile')
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile')
    else:
        form = LoginForm(request)

    # новая капча при каждом показе формы
    a, b = random.randint(1, 9), random.randint(1, 9)
    request.session['captcha_answer'] = a + b
    form.fields['captcha'].label = f'Капча: сколько будет {a} + {b}?'
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user,
        defaults={'phone': '', 'birth_date': '2000-01-01', 'city': ''},
    )
    return render(request, 'accounts/profile.html', {'profile': profile})