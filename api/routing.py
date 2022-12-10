from django.urls import path
from .consumer import GetGMJIConsumer, GetJAGIConsumer, GetPWJIConsumer
from .tests import FirebaseTest

ws_urlpatterns = [
    path('get_gmji_data/<str:name>/', GetGMJIConsumer.as_asgi()),
    path('get_jagi_data/<str:name>/', GetJAGIConsumer.as_asgi()),
    path('get_pwji_data/<str:name>/', GetPWJIConsumer.as_asgi()),
    # path('get_gmji_data_test/<str:name>/', FirebaseTest.as_asgi()),
]