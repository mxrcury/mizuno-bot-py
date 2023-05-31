import io
import os
import shutil
import pytube
from timeit import default_timer
start = None


def extract_audio(video_url):
    start = default_timer()
    youtube = pytube.YouTube(video_url)
    print(f"Downloading {youtube.title}...")
    audio_stream = youtube.streams.first()
    # filter(only_audio=True)
    # print("audio stream ->", audio_stream, "<- audio stream")
    audio_buffer = io.BytesIO()
    audio_stream.stream_to_buffer(audio_buffer)
    audio_buffer.seek(0)
    end = default_timer()
    return youtube.title, audio_buffer.getbuffer()
