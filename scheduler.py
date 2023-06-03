import asyncio
import aioschedule
from aiogram import types


class Scheduler:
    def __init__(self):
        self.__start_task()

    def __start_task(self):
        asyncio.create_task(self.send_message())

    def send_message(self, message: types.Message):
        message.answer("😎")
