"""
ASGI config for TSIR_System project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
#from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TSIR_System.settings')

#application = get_asgi_application()
# application=ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # WebSocket chat/notify
#     'websocket': URLRouter([
#         #path('ws/chat/<str:room>/', consumers.ChatConsumer),
#         #path('ws/notify/', consumers.NotifyConsumer)
#     ])
# })
