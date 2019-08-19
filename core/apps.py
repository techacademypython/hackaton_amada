from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    def ready(self):

        from mqtt.mqtt_file import client
        client.loop_start()
