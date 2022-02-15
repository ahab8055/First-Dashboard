from django.apps import AppConfig


class Module1Config(AppConfig):
    name = 'module1'

    def ready(self):
        from scheduler import updater
        updater.start()