from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Uczestnik
from django.contrib.messages import constants as messages
from cuser.models import CUser

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user, 'new_profile':new_profile})
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form':profile_form})


# Create your views here.
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def user_profile(request):
    current_user = request.user
    profile = Uczestnik.objects.get(user_id=CUser.objects.get(pk=2).pk)
    return render(request, 'accounts/profile.html', {'user': current_user, 'profile': profile})
        