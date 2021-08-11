from django.views.generic.edit import CreateView
from django.shortcuts import render


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
            return render(request, "accounts/register_done.html")

        context = {"user_form": user_form, "address_form": address_form, "participant_form": participant_form}
        return render(request, self.template_name, context)


from django.views.generic.detail import DetailView


class ParticipantDetailView(DetailView):
    # specify the model to use
    context_object_name = "participant"
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["address"] = Address.objects.get(user=context.email)
        context['extra'] = Participant.objects.get(user=context.email)
        return context
