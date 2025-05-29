import os
import platform
import warnings
from config import SoundConfig

class SoundPlayer:
    def __init__(self):
        self.enabled = SoundConfig.ENABLED
        self._init_sound_system()

    def _init_sound_system(self):
        if not self.enabled:
            return

        try:
            if platform.system() == "Windows":
                import winsound
                self.play_sound = lambda path: winsound.PlaySound(
                    path, winsound.SND_FILENAME | winsound.SND_ASYNC
                )
            else:
                import pygame
                pygame.mixer.init()
                self.play_sound = lambda path: pygame.mixer.Sound(path).play()
        except (ImportError, Exception) as e:
            self.enabled = False
            warnings.warn(f"Sound system not available: {str(e)}")

    def play_click(self):
        if self.enabled and hasattr(self, 'play_sound'):
            try:
                self.play_sound(SoundConfig.CLICK_SOUND)
            except Exception as e:
                warnings.warn(f"Error playing sound: {str(e)}")
                self.enabled = False