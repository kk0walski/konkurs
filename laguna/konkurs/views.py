from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from cuser.models import CUser
from django.views.generic.edit import CreateView
from .models import Uczestnik


def user_is_uczestnik(user):
    return Uczestnik.objects.filter(user_id=user.pk).exists()

#User Section

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
        profile_form = ProfileForm(
            request.POST, instance=Uczestnik.objects.get(user_id=request.user.pk))
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(
            instance=Uczestnik.objects.get(user_id=request.user.pk))
    return render(request, 'accounts/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


from .models import Uczestnik


@login_required
def user_profile(request):
    current_user = request.user
    if user_is_uczestnik(current_user):
        profile = Uczestnik.objects.get(user_id=request.user.pk)
        return render(request, 'accounts/profile.html', {'user': current_user, 'profile': profile})
    else:
        return render(request, 'accounts/reviewProfile.html', {'user': current_user})

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import WorkListFilter
from .models import Work
from .tables import WorkTable
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class WorkListView(SingleTableMixin, LoginRequiredMixin, FilterView):
    table_class = WorkTable
    model = Work
    template_name = 'works/list.html'
    filterset_class = WorkListFilter

    def get_queryset(self):
        if self.request.user.groups.exists() and self.request.user.groups.filter(name__in=Work.CATEGORY).exists():
            return Work.objects.filter(category__in=self.request.user.groups.values_list('name', flat=True))
        else:
            return Work.objects.all()

class FilteredWorkListView(SingleTableMixin, FilterView, LoginRequiredMixin, UserPassesTestMixin):
    table_class = WorkTable
    model = Work
    template_name = 'works/list.html'
    filterset_class = WorkListFilter

    def test_func(self):
        return user_is_uczestnik(self.request.user)

    def get_queryset(self):
        return Work.objects.filter(autor=Uczestnik.objects.get(user_id=self.request.user.pk))


from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Picture
from django.urls import reverse_lazy

#Picture Section

from .forms import PictureForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_picture(request):
    if request.method == 'POST':
        picture_form = PictureForm(request.POST, request.FILES)
        if picture_form.is_valid():
            picture = picture_form.save(commit=False)
            picture.autor = Uczestnik.objects.get(user_id=request.user.pk)
            picture.category = 'Picture'
            picture.save()
            print(request)
            messages.success(request, 'You addded picture')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        picture_form = PictureForm()
    return render(request, 'works/picture.html', {'picture': picture_form})

class PictureDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Picture
    template_name = 'worksDetail/picture_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PictureDetail, self).get_context_data(**kwargs)
        context['work'] = Work.objects.get(pk=self.kwargs['pk'])
        return context

class PictureUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Picture
    fields = fields = ['title', 'wymiary', 'opis',
                       'cena', 'obraz', 'technika', 'year']
    template_name = 'worksUpdate/picture_update.html'
    success_url = reverse_lazy('ListOfWorks')

    def test_func(self):
        return user_is_uczestnik(self.request.user)

#DigitalGraphics Section

from .forms import DigitalGraphicsForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_digitalGraphics(request):
    if request.method == 'POST':
        digitalGraphics_form = DigitalGraphicsForm(request.POST, request.FILES)
        if digitalGraphics_form.is_valid():
            digitalGraphics = digitalGraphics_form.save(commit=False)
            digitalGraphics.autor = Uczestnik.objects.get(user_id=request.user.pk)
            digitalGraphics.category = 'DigitalGraphics'
            digitalGraphics.save()
            messages.success(request, 'You addded digital graphics')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        digitalGraphics_form = DigitalGraphicsForm()
    return render(request, 'works/digitalGraphics.html', {'digitalGraphics': digitalGraphics_form})

from .models import DigitalGraphic

class DigitalGraphicsDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = DigitalGraphic
    template_name = 'worksDetail/digitalGraphics_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PictureDetail, self).get_context_data(**kwargs)
        context['work'] = Work.objects.get(pk=self.kwargs['pk'])
        return context


class DigitalGraphicsUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = DigitalGraphic
    fields = fields = ['title', 'obraz', 'opis', 'cena', 'year']
    template_name = 'worksUpdate/digitalGraphics_update.html'
    success_url = reverse_lazy('ListOfWorks')

    def test_func(self):
        return user_is_uczestnik(self.request.user)

#Sculpture Section

from .forms import SculptureForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_sculpture(request):
    if request.method == 'POST':
        sculpture_form = SculptureForm(request.POST, request.FILES)
        if sculpture_form.is_valid():
            sculpture = sculpture_form.save(commit=False)
            sculpture.autor = Uczestnik.objects.get(user_id=request.user.pk)
            sculpture.category = 'Sculpture'
            sculpture.save()
            messages.success(request, 'You addded sculpture')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        sculpture_form = SculptureForm()
    return render(request, 'works/sculpture.html', {'sculpture': sculpture_form})

from .models import Sculpture

class SculptureDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Sculpture
    template_name = 'worksDetail/Sculpture_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PictureDetail, self).get_context_data(**kwargs)
        context['work'] = Work.objects.get(pk=self.kwargs['pk'])
        return context


class SculptureUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Sculpture
    fields = fields = ['title', 'wymiary', 'opis', 'cena', 'obraz1',
                       'obraz2', 'obraz3', 'video_url', 'video_password', 'year']
    template_name = 'worksUpdate/Sculpture_update.html'
    success_url = reverse_lazy('ListOfWorks')

    def test_func(self):
        return user_is_uczestnik(self.request.user)

#Paint Section

from .forms import PaintForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_paint(request):
    if request.method == 'POST':
        paint_form = PaintForm(request.POST, request.FILES)
        if paint_form.is_valid():
            paint = paint_form.save(commit=False)
            paint.autor = Uczestnik.objects.get(user_id=request.user.pk)
            paint.category = 'Paint'
            paint.save()
            messages.success(request, 'You addded paint')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        paint_form = PaintForm()
    return render(request, 'works/paint.html', {'paint': paint_form})

from .models import Paint

class PaintDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Paint
    template_name = 'worksDetail/Paint_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PictureDetail, self).get_context_data(**kwargs)
        context['work'] = Work.objects.get(pk=self.kwargs['pk'])
        return context

class PaintUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Paint
    fields = fields = ['title', 'wymiary', 'opis', 'cena',
                       'obraz', 'technika', 'year']
    template_name = 'worksUpdate/Paint_update.html'
    success_url = reverse_lazy('ListOfWorks')

    def test_func(self):
        return user_is_uczestnik(self.request.user)

#VirtualArt section

from .forms import VirtualArtForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_virtualart(request):
    if request.method == 'POST':
        virtualArt_form = VirtualArtForm(request.POST, request.FILES)
        if virtualArt_form.is_valid():
            virtualArt = virtualArt_form.save(commit=False)
            virtualArt.autor = Uczestnik.objects.get(user_id=request.user.pk)
            virtualArt.category = 'VirtualArt'
            virtualArt.save()
            messages.success(request, 'You addded virtual art')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        virtualArt_form = VirtualArtForm()
    return render(request, 'works/virtualArt.html', {'virtualArt': virtualArt_form})

from .models import VirtualArt

class VirtualArtDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = VirtualArt
    template_name = 'worksDetail/VirtualArt_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PictureDetail, self).get_context_data(**kwargs)
        context['work'] = Work.objects.get(pk=self.kwargs['pk'])
        return context

class VirtualArtUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = VirtualArt
    fields = fields = ['title', 'wymiary', 'opis', 'cena', 'obraz1',
                       'obraz2', 'obraz3', 'video_url', 'video_password', 'year']
    template_name = 'worksUpdate/VirtualArt_update.html'
    success_url = reverse_lazy('ListOfWorks')

    def test_func(self):
        return user_is_uczestnik(self.request.user)

#Video Section

from .forms import VideoForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_video(request):
    if request.method == 'POST':
        video_form = VideoForm(request.POST, request.FILES)
        if video_form.is_valid():
            video = video_form.save(commit=False)
            video.autor = Uczestnik.objects.get(user_id=request.user.pk)
            video.category = 'Video'
            video.save()
            messages.success(request, 'You addded video')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        video_form = VideoForm()
    return render(request, 'works/video.html', {'video': video_form})



from .models import Video

class VideoDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Video
    template_name = 'worksDetail/Video_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PictureDetail, self).get_context_data(**kwargs)
        context['work'] = Work.objects.get(pk=self.kwargs['pk'])
        return context

class VideoUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Video
    fields = fields = ['title', 'time', 'opis', 'cena', 'obraz',
                       'year', 'video_url', 'video_password']
    template_name = 'worksUpdate/Video_update.html'
    success_url = reverse_lazy('ListOfWorks')

    def test_func(self):
        return user_is_uczestnik(self.request.user)

#Performence Section

from .forms import PerformenceForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_performence(request):
    if request.method == 'POST':
        performence_form = PerformenceForm(request.POST, request.FILES)
        if performence_form.is_valid():
            performence = performence_form.save(commit=False)
            performence.autor = Uczestnik.objects.get(user_id=request.user.pk)
            performence.category = 'Performence'
            performence.save()
            messages.success(request, 'You addded performence')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        performence_form = PerformenceForm()
    return render(request, 'works/performence.html', {'performence': performence_form})


from .models import Performence

class PerformenceDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Performence
    template_name = 'worksDetail/Performence_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PictureDetail, self).get_context_data(**kwargs)
        context['work'] = Work.objects.get(pk=self.kwargs['pk'])
        return context

class PerformenceUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Performence
    fields = fields = ['title', 'time', 'opis', 'cena', 'obraz',
                       'year', 'video_url', 'video_password']
    template_name = 'worksUpdate/Performence_update.html'
    success_url = reverse_lazy('ListOfWorks')

    def test_func(self):
        return user_is_uczestnik(self.request.user)

#LandArt Section

from .forms import LandArtForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_landArt(request):
    if request.method == 'POST':
        landArt_form = LandArtForm(request.POST, request.FILES)
        if landArt_form.is_valid():
            landArt = landArt_form.save(commit=False)
            landArt.autor = Uczestnik.objects.get(user_id=request.user.pk)
            landArt.category = 'LandArt'
            landArt.save()
            messages.success(request, 'You addded landArt')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        landArt_form = LandArtForm()
    return render(request, 'works/landArt.html', {'landArt': landArt_form})

from .models import LandArt

class LandArtDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = LandArt
    template_name = 'worksDetail/LandArt_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PictureDetail, self).get_context_data(**kwargs)
        context['work'] = Work.objects.get(pk=self.kwargs['pk'])
        return context
class LandArtUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = LandArt
    fields = fields = ['title', 'obraz1', 'obraz2', 'obraz3', 'opis']
    template_name = 'worksUpdate/LandArt_update.html'
    success_url = reverse_lazy('ListOfWorks')

    def test_func(self):
        return user_is_uczestnik(self.request.user)

#UrbanArt Section

from .forms import UrbanArtForm

@login_required
@user_passes_test(user_is_uczestnik)
def add_urbanArt(request):
    if request.method == 'POST':
        urbanArt_form = UrbanArtForm(request.POST, request.FILES)
        if urbanArt_form.is_valid():
            urbanArt = urbanArt_form.save(commit=False)
            urbanArt.autor = Uczestnik.objects.get(user_id=request.user.pk)
            urbanArt.category = 'UrbanArt'
            urbanArt.save()
            messages.success(request, 'You addded urban art')
            return render(request, 'accounts/profile.html', {'user': request.user, 'profile': Uczestnik.objects.get(user_id=request.user.pk)})
        else:
            messages.error(request,  'Please correct the error below.')
    else:
        urbanArt_form = UrbanArtForm()
    return render(request, 'works/urbanArt.html', {'urbanArt': urbanArt_form})

from .models import UrbanArt


class UrbanArtDetail(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = UrbanArt
    template_name = 'worksDetail/UrbanArt_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PictureDetail, self).get_context_data(**kwargs)
        context['work'] = Work.objects.get(pk=self.kwargs['pk'])
        return context
class UrbanArtUpdate(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = UrbanArt
    fields = fields = ['title', 'obraz1', 'obraz2', 'obraz3', 'opis']
    template_name = 'worksUpdate/UrbanArt_update.html'
    success_url = reverse_lazy('ListOfWorks')

    def test_func(self):
        return user_is_uczestnik(self.request.user)

def update_average(request, id):
    work = Work.objects.get(pk=id);
    rate = work.ratings.get_queryset()[0]
    work.average = rate.average
    work.save()
    return redirect('ListOfWorks')