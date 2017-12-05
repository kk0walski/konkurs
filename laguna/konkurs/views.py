from django.shortcuts import render
from .forms import UczestnikForm
from django.shortcuts import redirect

# Create your views here.
def uczestnik_new(request):
    if request.method == 'POST':
        form = UczestnikForm(request.POST)
        if form.is_valid():
            uczestnik = form.save(commit=False)
            uczestnik.save()
            return redirect('workpost', pk=uczestnik.pk)
    else:
        form = UczestnikForm()
    return render(request, 'zgloszenie.html', {'form' : form})