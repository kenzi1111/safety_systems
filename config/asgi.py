import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat import routing


# プロトコルごとの分岐処理
application = ProtocolTypeRouter(
    {
        # httpの場合：これまで通り処理
        "http": django_asgi_app,
        # websocketの場合：ALLOWED_HOSTSの検証、ユーザ認証が実施されていることを確認
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                # 問題なければ、routing.pyの内容に基づいてルーティングを実施
                URLRouter(routing.websocket_urlpatterns)
            )
        ),
    }
)
