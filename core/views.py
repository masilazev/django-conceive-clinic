from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('dashboard')
        else:
            context = {
                'error_message': 'Credenciais inválidas. Verifique seu usuário e senha.'
            }
            return render(request, 'core/login.html', context)

    return render(request, 'core/login.html')


@login_required
def dashboard_view(request):
    context = {
        'username': request.user.username,
    }
    return render(request, 'core/dashboard.html', context)
