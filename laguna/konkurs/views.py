from django.shortcuts import render
from .forms import UczestnikForm

# Create your views here.
def uczestnik_new(request):
    if request.method == 'POST':
        form = UczestnikForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UczestnikForm()
    return render(request, 'zgloszenie.html', {'form' : form})