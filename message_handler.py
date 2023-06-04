from aiogram import types
from extractor import extract_audio


class MessageHandler:
    def __init__(self):
        pass

    async def start(self, message: types.Message):
        await message.answer("Hello! I'm a Mizuno.\nTelegram bot for downloading youtube videos and music")

    async def extract_audio(self, message: types.Message):
        arguments = message.text.split(' ')
        is_link = arguments.__len__() > 1

        if is_link:
            link = arguments[1]
            audio_title, audio_buffer = extract_audio(link)
            await message.answer_audio(
                title=audio_title,
                audio=audio_buffer,
                caption="Music was downloaded by @mizuno_chan_bot💮🇯🇵",
                performer=audio_title
            )
        else:
            await message.answer("You have not provide a link")


message_handler = MessageHandler()
