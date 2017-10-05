from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def me(request):
    return render(request, 'users/user_details.html')