from django.urls import path
from django.conf import settings
from .views import works, update_profile, Register, user_profile, add_sculpture, add_paint, add_picture,add_virtualart, add_video, add_landArt, add_urbanArt, add_digitalGraphics
from django.contrib.auth.views import login, logout
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
    path('profile/works', works, name="ListOfWorks")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)