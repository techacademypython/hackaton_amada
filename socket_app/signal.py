# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# from core.models import *
# import  datetime
#
# channel_layer = get_channel_layer()
#
# from datetime import datetime
# now = datetime.now()
#
#
# @receiver(post_save, sender=CordinateAndTempureture, dispatch_uid="in_cordinate")
# def in_cordinate(sender, **kwargs):
#     notification = kwargs.get('instance')
#     created = kwargs.get('created')
#     channel_layer = get_channel_layer()
#
#     if created:
#         context = {
#             "imei": notification.imei.imei,
#             "point": notification.point,
#             "tempureture": notification.tempureture,
#             "humudity": notification.humudity,
#             "pressure": notification.pressure
#         }
#         print(context)
#         async_to_sync(channel_layer.group_send)("notification",
#                                                 {"type": "send_coordainate_message",
#                                                  "data": context})
#
# @receiver(post_save, sender=Notfication, dispatch_uid="in_notfication")
# def in_notfication(sender, **kwargs):
#     notification = kwargs.get('instance')
#     created = kwargs.get('created')
#
#     if created:
#
#         date_time = now.strftime("%H:%M:%S, %d/%m/%Y")
#
#         context = {
#                    "notfication_type": notification.notification_type,
#                    "device": notification.device.imei,
#                     "by": notification.by_who,
#                    "created_at": date_time,
#                    }
#         async_to_sync(channel_layer.group_send)("notification",
#                                                 {"type": "send_notification_message",
#                                                  "data": context})
#
#
#
