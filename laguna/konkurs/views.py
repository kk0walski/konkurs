from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from cuser.models import CUser
from django.views.generic.edit import CreateView


def user_is_uczestnik(user):
    return Uczestnik.objects.filter(user_id=user.pk).exists()

from .forms import UserForm, ProfileForm

class Register(CreateView):
    form_class = UserForm
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        user_form = UserForm()
        profile_form = ProfileForm()
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

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
            return render(request, 'accounts/register_done.html')
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

from .forms import UserEditForm, ProfileForm
from django.db import transaction
# Create your views here.
@login_required
@transaction.atomic
@user_passes_test(user_is_uczestnik)
def update_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=Uczestnik.objects.get(user_id=request.user.pk))
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=Uczestnik.objects.get(user_id=request.user.pk))
    return render(request, 'accounts/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

from .models import Uczestnik

@login_required
@user_passes_test(user_is_uczestnik)
def user_profile(request):
    current_user = request.user
    profile = Uczestnik.objects.get(user_id=request.user.pk)
    return render(request, 'accounts/profile.html', {'user': current_user, 'profile': profile})

from .forms import SculptureForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_sculpture(request):
    if request.method == 'POST':
        sculpture_form = SculptureForm(request.POST, request.FILES)
        if sculpture_form.is_valid():
            sculpture = sculpture_form.save(commit=False)
            sculpture.autor = Uczestnik.objects.get(user_id = request.user.pk)
            sculpture.category = 'Sculpture'
            sculpture.save()
            messages.success(request, 'You addded sculpture')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        sculpture_form = SculptureForm()
    return render(request, 'works/sculpture.html', {'sculpture': sculpture_form})

from .forms import PaintForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_paint(request):
    if request.method == 'POST':
        paint_form = PaintForm(request.POST, request.FILES)
        if paint_form.is_valid():
            paint = paint_form.save(commit=False)
            paint.autor = Uczestnik.objects.get(user_id = request.user.pk)
            paint.category = 'Paint'
            paint.save()
            messages.success(request, 'You addded paint')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        paint_form = PaintForm()
    return render(request, 'works/paint.html', {'paint': paint_form})

from .forms import PictureForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_picture(request):
    if request.method == 'POST':
        picture_form = PictureForm(request.POST, request.FILES)
        if picture_form.is_valid():
            picture = picture_form.save(commit=False)
            picture.autor = Uczestnik.objects.get(user_id = request.user.pk)
            picture.category = 'Picture'
            picture.save()
            messages.success(request, 'You addded picture')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        picture_form = PictureForm()
    return render(request, 'works/picture.html', {'picture': picture_form})

from .forms import VirtualArtForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_virtualart(request):
    if request.method == 'POST':
        virtualArt_form = VirtualArtForm(request.POST, request.FILES)
        if  virtualArt_form.is_valid():
            virtualArt = virtualArt_form.save(commit=False)
            virtualArt.autor = Uczestnik.objects.get(user_id = request.user.pk)
            virtualArt.category = 'VirtualArt'
            virtualArt.save()
            messages.success(request, 'You addded virtual art')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        virtualArt_form = VirtualArtForm()
    return render(request, 'works/virtualArt.html', {'virtualArt': virtualArt_form})

from .forms import VideoForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_video(request):
    if request.method == 'POST':
        video_form = VideoForm(request.POST)
        if video_form.is_valid():
            video = video_form.save(commit=False)
            video.autor = Uczestnik.objects.get(user_id = request.user.pk)
            video.category = 'Video'
            video.save()
            messages.success(request, 'You addded video')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        video_form = VideoForm()
    return render(request, 'works/video.html', {'video': video_form})

from .forms import PerformenceForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_performence(request):
    if request.method == 'POST':
        performence_form = PerformenceForm(request.POST, request.FILES)
        if performence_form.is_valid():
            performence = performence_form.save(commit=False)
            performence.autor = Uczestnik.objects.get(user_id = request.user.pk)
            performence.category = 'Performence'
            performence.save()
            messages.success(request, 'You addded performence')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        performence_form = PerformenceForm()
    return render(request, 'works/performence.html', {'performence': performence_form})

from .forms import LandArtForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_landArt(request):
    if request.method == 'POST':
        landArt_form = LandArtForm(request.POST, request.FILES)
        if landArt_form.is_valid():
            landArt = landArt_form.save(commit=False)
            landArt.autor = Uczestnik.objects.get(user_id = request.user.pk)
            landArt.category = 'LandArt'
            landArt.save()
            messages.success(request, 'You addded landArt')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        landArt_form = LandArtForm()
    return render(request, 'works/landArt.html', {'landArt': landArt_form})

from .forms import UrbanArtForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_urbanArt(request):
    if request.method == 'POST':
        urbanArt_form = UrbanArtForm(request.POST, request.FILES)
        if urbanArt_form.is_valid():
            urbanArt = urbanArt_form.save(commit=False)
            urbanArt.autor = Uczestnik.objects.get(user_id = request.user.pk)
            urbanArt.category = 'UrbanArt'
            urbanArt.save()
            messages.success(request, 'You addded urban art')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        urbanArt_form = UrbanArtForm()
    return render(request, 'works/urbanArt.html', {'urbanArt': urbanArt_form})

from .forms import DigitalGraphicsForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_digitalGraphics(request):
    if request.method == 'POST':
        digitalGraphics_form = DigitalGraphicsForm(request.POST, request.FILES)
        if digitalGraphics_form.is_valid():
            digitalGraphics = digitalGraphics_form.save(commit=False)
            digitalGraphics.autor = Uczestnik.objects.get(user_id = request.user.pk)
            digitalGraphics.category = 'DigitalGraphics'
            digitalGraphics.save()
            messages.success(request, 'You addded digital graphics')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        digitalGraphics_form = DigitalGraphicsForm()
    return render(request, 'works/digitalGraphics.html', {'digitalGraphics': digitalGraphics_form})

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import WorkListFilter
from .models import Work
from .tables import WorkTable
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class FilteredWorkListView(SingleTableMixin, FilterView, LoginRequiredMixin, UserPassesTestMixin):
    table_class = WorkTable
    model = Work
    template_name = 'works/list.html'
    filterset_class = WorkListFilter
    
    def test_func(self):
        return user_is_uczestnik(self.request.user)

    def get_queryset(self):
        return Work.objects.filter(autor = Uczestnik.objects.get(user_id = self.request.user.pk))

from django.views.generic.detail import DetailView
from .models import Picture

class PictureDetail(DetailView):
    model = Picture
    template_name = 'worksDetail/picture_detail.html'