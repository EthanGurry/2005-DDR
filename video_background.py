import pygame
import threading
from moviepy.editor import VideoFileClip

def play_video_background(video_path, screen):
    def play_video():
        clip = VideoFileClip(video_path).resize((800, 600))
        clip.preview(fullscreen=False)

    video_thread = threading.Thread(target=play_video)
    video_thread.start()
    return video_thread
