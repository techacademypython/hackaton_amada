from django.contrib import admin
from core.models import  *
# Register your models here.


@admin.register(Notfication)
class NotficationAdmin(admin.ModelAdmin):
    pass

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass

# @admin.register(CordinateAndTempureture)
# class CordinateAndTempuretureAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(KeyCheker)
# class KeyChekerAdmin(admin.ModelAdmin):
#     pass
