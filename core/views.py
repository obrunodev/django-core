from django.shortcuts import redirect


def index(request):
    user = request.user
    
    if not user.is_authenticated:
        return redirect('users:login')

    if user.is_superuser:
        return redirect('patients:list')
    else:
        return redirect('recipes:showroom')