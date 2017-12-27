from django.contrib import admin
from .models import Uczestnik
from .models import Uczestnik, Sculpture, Paint, VirtualArt, DigitalGraphic, Picture, Video, Performence, LandArt, UrbanArt

# Register your models here.
admin.site.register(Uczestnik)
admin.site.register(Sculpture)
admin.site.register(Paint)
admin.site.register(VirtualArt)
admin.site.register(DigitalGraphic)
admin.site.register(Picture)
admin.site.register(Video)
admin.site.register(Performence)
admin.site.register(LandArt)
admin.site.register(UrbanArt)