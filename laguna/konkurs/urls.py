from django.urls import path
from .views import PerformenceDetail, LandArtDetail, UrbanArtDetail
from .views import PaintDetail, VirtualArtDetail, DigitalGraphicsDetail, VideoDetail
from .views import FilteredWorkListView, update_profile, Register, PictureDetail, SculptureDetail
from .views import user_profile, add_sculpture, add_paint, add_picture
from .views import add_virtualart, add_video, add_landArt, add_urbanArt, add_digitalGraphics
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', login, name='login'),
    path('profile/', user_profile, name='profile'),
    path('logout/', logout, name='logout', kwargs={'next_page' : '/'}),
    path('profile/sculpture', add_sculpture, name='sculpture'),
    path('profile/paint', add_paint, name='paint'),
    path('profile/picture', add_picture, name='picture'),
    path('profile/virtualArt', add_virtualart, name='virtualArt'),
    path('profile/video', add_video, name='video'),
    path('profile/performence', add_video, name='performence'),
    path('profile/landArt', add_landArt, name='landArt'),
    path('profile/urbanArt', add_urbanArt, name='urbanArt'),
    path('profile/digitalGraphics', add_digitalGraphics, name='digitalGraphics'),
    path('profile/edit', update_profile, name="updateProfile"),
    path('profile/works', FilteredWorkListView.as_view(), name="ListOfWorks"),
    path('profile/works/Picture/<int:pk>', PictureDetail.as_view(), name="Picture"),
    path('profile/works/Sculpture/<int:pk>', SculptureDetail.as_view(), name="Sculpture"),
    path('profile/works/Paint/<int:pk>', PaintDetail.as_view(), name="Paint"),
    path('profile/works/VirtualArt/<int:pk>', VirtualArtDetail.as_view(), name="VirtualArt"),
    path('profile/works/DigitalGraphic/<int:pk>', DigitalGraphicsDetail.as_view(), name="DigitalGraphic"),
    path('profile/works/Video/<int:pk>', VideoDetail.as_view(), name="Video"),
    path('profile/works/Performence/<int:pk>', PerformenceDetail.as_view(), name="Performence"),
    path('profile/works/LandArt/<int:pk>', LandArtDetail.as_view(), name="LandArt"),
        path('profile/works/UrbanArt/<int:pk>', UrbanArtDetail.as_view(), name="UrbanArt"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)