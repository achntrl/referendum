from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.forms import AccountProfileForm


@login_required(login_url='/login')
def me(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AccountProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountProfileForm()
    return render(request, 'account/user_details.html', {'form': form})
