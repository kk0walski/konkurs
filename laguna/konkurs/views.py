from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm, SculptureForm, PaintForm, PictureForm, VirtualArtForm, VideoForm, PerformenceForm, LandArtForm, UrbanArtForm, DigitalGraphicsForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from .models import Uczestnik
from django.contrib import messages
from cuser.models import CUser
from django.views.generic.edit import CreateView

def user_is_uczestnik(user):
    return Uczestnik.objects.filter(user_id=user.pk).exists()

class Register(CreateView):
    form_class = UserForm
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        user_form = UserForm()
        profile_form = ProfileForm()
        return render(request, self.template_name, {'user_form': user_form, 'profile_form':profile_form})

    def post(self, request, *args, **kwargs):
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
        return render(request, self.template_name, {'user_form': user_form, 'profile_form':profile_form})


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
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('settings:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
@user_passes_test(user_is_uczestnik)
def user_profile(request):
    current_user = request.user
    profile = Uczestnik.objects.get(user_id=request.user.pk)
    return render(request, 'accounts/profile.html', {'user': current_user, 'profile': profile})
        
@login_required
def add_sculpture(request):
    if request.method == 'POST':
        sculpture = SculptureForm(request.POST)
        sculpture.author = request.user
        if sculpture.is_valid():
            sculpture.save()
            messages.success(request, 'You addded sculpture')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        sculpture = SculptureForm()
    return render(request, 'works/sculpture.html', {'sculpture': sculpture})

@login_required
def add_paint(request):
    if request.method == 'POST':
        paint = PaintForm(request.POST)
        paint.author = request.user
        if paint.is_valid():
            paint.save()
            messages.success(request, 'You addded paint')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        paint = PaintForm()
    return render(request, 'works/paint.html', {'paint': paint})

class CreatePicture(CreateView):
    form_class = PictureForm
    template_name = 'works/picture.html'

    def get(self, request, *args, **kwargs):
        picture_form = PictureForm()
        return render(request, self.template_name, {'picture': picture_form})
    
    @login_required
    @user_passes_test(user_is_uczestnik)
    def post(self, request, *args, **kwargs):
        picture_form = PictureForm(request.POST, request.FILES)
        if picture_form.is_valid():
            picture = picture_form.save(commit=False)
            picture.author = Uczestnik.objects.get(pk=request.user.pk)
            image = request.FILES['obraz']
            picture.save(image.name, image)
            messages.success(request, 'You addded picture')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        return render(request, self.template_name, {'picture': picture})

@login_required
def add_virtualart(request):
    if request.method == 'POST':
        virtualArt = VirtualArtForm(request.POST)
        virtualArt.author = request.user
        if virtualArt.is_valid():
            virtualArt.save()
            messages.success(request, 'You addded virtual art')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        virtualArt = VirtualArtForm()
    return render(request, 'works/virtualArt.html', {'virtualArt': virtualArt})

@login_required
def add_video(request):
    if request.method == 'POST':
        video = VideoForm(request.POST)
        video.author = request.user
        if video.is_valid():
            video.save()
            messages.success(request, 'You addded video')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        video = VideoForm()
    return render(request, 'works/video.html', {'video': video})

@login_required
def add_performence(request):
    if request.method == 'POST':
        performence = PerformenceForm(request.POST)
        performence.author = request.user
        if performence.is_valid():
            performence.save()
            messages.success(request, 'You addded performence')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        performence = PerformenceForm()
    return render(request, 'works/performence.html', {'performence': performence})

@login_required
def add_landArt(request):
    if request.method == 'POST':
        landArt = LandArtForm(request.POST)
        landArt.author = request.user
        if landArt.is_valid():
            landArt.save()
            messages.success(request, 'You addded landArt')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        landArt = LandArtForm()
    return render(request, 'works/landArt.html', {'landArt': landArt})

@login_required
def add_urbanArt(request):
    if request.method == 'POST':
        urbanArt = UrbanArtForm(request.POST)
        urbanArt.author = request.user
        if urbanArt.is_valid():
            urbanArt.save()
            messages.success(request, 'You addded urban art')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        urbanArt = UrbanArtForm()
    return render(request, 'works/urbanArt.html', {'urbanArt': urbanArt})

@login_required
def add_digitalGraphics(request):
    if request.method == 'POST':
        digitalGraphics = DigitalGraphicsForm(request.POST)
        digitalGraphics.author = request.user
        if digitalGraphics.is_valid():
            digitalGraphics.save()
            messages.success(request, 'You addded digital graphics')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        digitalGraphics = DigitalGraphicsForm()
    return render(request, 'works/digitalGraphics.html', {'digitalGraphics': digitalGraphics})