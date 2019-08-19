# from channels.exceptions import DenyConnection
# from channels.generic.websocket import AsyncWebsocketConsumer
# import  json
#
#
# class NotificationWebsocket(AsyncWebsocketConsumer):
#
#     async def connect(self):
#         self.room_name = self.scope['user'].id
#         # print(self.room_name)
#         self.room_group_name = 'notification'
#         # print(self.room_group_name)
#
#         self.user = self.scope['user']
#         # Join room group
#         if self.user.username:
#             await self.channel_layer.group_add(
#                 self.room_group_name,
#                 self.channel_name
#             )
#
#             await self.accept()
#
#             # await self.accept()
#
#             self.data = {
#                 "data": [1,2,3]
#             }
#
#             await self.send(text_data=json.dumps({
#                 "data": self.data
#             }))
#         else:
#             raise DenyConnection("Connection closed")
#
#     # Receive message from WebSocket
#     # async def receive(self, text_data):
#     #     text_data_json = json.loads(text_data)
#     #     print(self.user.id)
#     #     await self.send(text_data=json.dumps({
#     #         "count": 0,
#     #         "data": text_data_json
#     #     }))
#
#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from room group
#     async def send_notification_message(self, event):
#         data = event['data']
#         print(data)
#
#         # print(message)
#         # print(message)
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps(data))
#     #
#     async def send_coordainate_message(self, event):
#         data = event['data']
#         print(data)
#
#         # print(message)
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps(data))