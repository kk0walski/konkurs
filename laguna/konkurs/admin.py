from django.contrib import admin
from cuser.models import CUser
from .models import Uczestnik, Sculpture, Paint, VirtualArt, DigitalGraphic, Picture, Video, Performence, LandArt, UrbanArt, Review

class ReviewInstanceInline(admin.TabularInline):
    model = Review

    
class PictureAdmin(admin.ModelAdmin):
    inlines = [ReviewInstanceInline]
    """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['queryset'] = CUser.objects.filter(email=request.user.email)
        return super(PictureAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('author',)
        return self.readonly_fields + ('author',)

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['author'] = request.user
        request.GET = data
        return super(PictureAdmin, self).add_view(request, form_url="", extra_context=extra_context)
    """

# Register your models here.
admin.site.register(Uczestnik)
admin.site.register(Sculpture)
admin.site.register(Paint)
admin.site.register(VirtualArt)
admin.site.register(DigitalGraphic)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Review)
admin.site.register(Video)
admin.site.register(Performence)
admin.site.register(LandArt)
admin.site.register(UrbanArt)