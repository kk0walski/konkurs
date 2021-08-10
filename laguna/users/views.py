from django.views.generic.edit import CreateView
from django.shortcuts import render


from .forms import UserForm, AddressCreateForm
from .models import CustomUser

# Create your views here.
class Register(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'registration/register.html'

    def get(self, request):
        user_form = UserForm()
        address_form = AddressCreateForm()
        context = {'user_form': user_form, 'address_form': address_form}
        return render(request, self.template_name, context)

    def post(self, request):
        user_form = UserForm(request.POST)
        address_form = AddressCreateForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_address = address_form.save(commit=False)
            new_address.user = new_user
            new_address.save()
            return render(request, 'accounts/register_done.html')

        context = {'user_form': user_form, 'address_form': address_form}
        return render(request, self.template_name, context)