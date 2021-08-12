from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect


from .forms import UserForm, AddressCreateForm, ParticipantForm
from .models import CustomUser, Address, Participant

# Create your views here.
class Register(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = "registration/register.html"

    def get(self, request):
        user_form = UserForm()
        participant_form = ParticipantForm()
        address_form = AddressCreateForm()
        context = {"user_form": user_form, "address_form": address_form, "participant_form": participant_form}
        return render(request, self.template_name, context)

    def post(self, request):
        user_form = UserForm(request.POST)
        address_form = AddressCreateForm(request.POST)
        participant_form = ParticipantForm(request.POST)
        if user_form.is_valid() and address_form.is_valid() and participant_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            new_address = address_form.save(commit=False)
            new_address.user = new_user
            new_address.save()
            new_participant = participant_form.save(commit=False)
            new_participant.user = new_user
            new_participant.save()
            return redirect('index')

        context = {"user_form": user_form, "address_form": address_form, "participant_form": participant_form}
        return render(request, self.template_name, context)


from django.contrib.auth.decorators import login_required

def user_is_uczestnik(user):
    """user_is_uczestnik.
    :return: True if user is uczestnik"""
    return Participant.objects.filter(user=user.email).exists()

@login_required
def user_profile(request):
    current_user = request.user
    if user_is_uczestnik(current_user):
        profile = Participant.objects.get(user=current_user.email)
        address = Address.objects.get(user=current_user.email)
        return render(request, 'accounts/profile.html', {'user': current_user, 'profile': profile, 'address': address})
    else:
        render(request, 'accounts/reviewProfile.html', {'user': current_user})
