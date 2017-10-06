from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.forms import UserChangeForm, CustomUserCreationForm


@login_required(login_url='/login')
def me(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserChangeForm(request.POST)
        if form.is_valid():
            request.user.save()
    else:
        form = UserChangeForm()
    return render(request, 'account/user_details.html', {'form': form})
