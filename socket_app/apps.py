from django.apps import AppConfig


class SocketAppConfig(AppConfig):
    name = 'socket_app'

    def ready(self):
        import socket_app.signal
