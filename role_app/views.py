from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            print("no no no invalid")
            pass

    return render(request, 'login.html')


@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')  

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def dashboard(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    else:
        return redirect('user_dashboard')
