from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Device(models.Model):
    imei = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    device_lat = models.FloatField( null=True, blank=True)  # kordinat saxlayir
    device_long = models.FloatField(null=True, blank=True)  # kordinat saxlayir
    tempureture = models.CharField(max_length=255, null=True, blank=True)  # tempturatur
    humudity = models.IntegerField( blank=True, null=True)  # rutubet faizle gostereciyik
    pressure = models.CharField(max_length=255, blank=True, null=True)  # teziq
    time_s = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.imei}"


    def new_info(self):
        return "/static/amada/images/car_marker_green.svg"

    def get_cordinates(self):
        return  f"{self.device_lat}, {self.device_long}"


class Notfication(models.Model):
    types = (
            ('Nolu cihaz açıldı', ' Nolu cihaz açıldı'),
            ('Nolu cihazı açmağa_cəhd_göstərildi', 'Nolu cihazı açmağa cəhd göstərildi'),
        )
    notification_type = models.CharField(max_length=50, choices=types, null=True, blank=True)
    device = models.ForeignKey(Device,  on_delete=models.CASCADE)
    time_s = models.CharField(max_length=255, null=True, blank=True)
    by_who = models.CharField(max_length=255, null=True, blank=True)



    def __str__(self):
        return "{} ".format(self.device.imei)

    class Meta:
        verbose_name = "Info Notfication"
        verbose_name_plural = "Info Notifications"

    def get_value(self):
        result = ''
        if self.notification_type == 'attempt_true':
            result = '{} -Nolu cihaz açıldı'.format(self.device.imei)

        elif self.notification_type == 'attempt_fails':
            result = '{} -Nolu açmağa cəhd göstərildi'.format(self.device.imei)

        return result

    def notfication(self):
        return f"{self.notification_type} {self.device.imei}, {self.time_s}"

