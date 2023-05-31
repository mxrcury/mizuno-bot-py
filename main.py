import logging
import os
from dotenv_vault import load_dotenv
from dataclasses import dataclass
from aiogram import Bot as TGBot, executor as dispatch_executor, types, Dispatcher
from message_handler import message_handler

load_dotenv()


class Bot:
    token: str
    bot: TGBot
    dp: Dispatcher

    def __init__(self, executor: dispatch_executor):
        self.__start(executor)

    def __start(self, executor: dispatch_executor):
        logging.basicConfig(level=logging.INFO)
        self.token = os.getenv("TOKEN")
        self.bot = TGBot(token=self.token)
        self.dp = Dispatcher(self.bot)
        self.register_handlers()
        executor.start_polling(self.dp)

    def register_handlers(self):
        self.dp.register_message_handler(
            message_handler.start, commands=["start"])
        self.dp.register_message_handler(
            message_handler.extract_audio, commands=["extract_audio"])


if __name__ == "__main__":
    Bot(executor=dispatch_executor)
