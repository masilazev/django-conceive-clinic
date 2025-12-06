from django.shortcuts import render

# Esta View renderiza o template de login.


def login_view(request):
    return render(request, 'core/login.html')
