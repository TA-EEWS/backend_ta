from django.test import TestCase
from channels.generic.websocket import AsyncWebsocketConsumer
import json

from .models import *
# Create your tests here.

class FirebaseTest(AsyncWebsocketConsumer):
    async def connect(self):
        name = self.scope['url_route']['kwargs']['name']
        
        for i in range(1000):
            lst = get_GMJI_data_firebase(name)
            self.send(json.dumps({
                'E_data':lst[0]['data'],
                'N_data':lst[1]['data'],
                'Z_data':lst[2]['data']
                }))
        await self.close()
        
    async def disconnect(self, code):
        return await super().disconnect(code)