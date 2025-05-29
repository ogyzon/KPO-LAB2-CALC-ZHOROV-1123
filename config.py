import os
from pathlib import Path

# Основные настройки приложения
class AppConfig:
    TITLE = "Калькулятор Жоров Макаров Сотвалдиев 1123"
    GEOMETRY = "400x600"
    MIN_WIDTH = 300
    MIN_HEIGHT = 500
    ABOUT_INFO = "Разработали студенты группы 10701123:\nМакаров А.С.\nЖоров Е.А.\nСотвалдиев А.С."

# Настройки тем
class ThemeConfig:
    MODE = "light"  # Можно менять на "dark"

    THEMES = {
        "light": {
            "BACKGROUND": "#f0f0f0",
            "FOREGROUND": "#000000",
            "BUTTON_BG": "#e0e0e0"
        },
        "dark": {
            "BACKGROUND": "#222222",
            "FOREGROUND": "#FFFFFF",
            "BUTTON_BG": "#444444"
        }
    }

    BACKGROUND = THEMES[MODE]["BACKGROUND"]
    FOREGROUND = THEMES[MODE]["FOREGROUND"]
    BUTTON_BG = THEMES[MODE]["BUTTON_BG"]

    @staticmethod
    def update_theme(mode):
        ThemeConfig.MODE = mode
        ThemeConfig.BACKGROUND = ThemeConfig.THEMES[mode]["BACKGROUND"]
        ThemeConfig.FOREGROUND = ThemeConfig.THEMES[mode]["FOREGROUND"]
        ThemeConfig.BUTTON_BG = ThemeConfig.THEMES[mode]["BUTTON_BG"]


# Настройки шрифтов
class FontConfig:
    FONT_NAME = "SF Pro Text"
    DISPLAY_SIZE = 24
    BUTTON_SIZE = 14
    FONT_PATH = os.path.join("resources", "fonts", "SFProText-Regular.ttf")

# Настройки иконки
class IconConfig:
    ICON_PATH = os.path.join("resources", "icons", "calculator_icon.ico")

# Настройки кнопок
class ButtonConfig:
    BACKGROUND = ThemeConfig.BUTTON_BG
    FOREGROUND = ThemeConfig.FOREGROUND
    BORDER_WIDTH = 0
    PADDING_X = 5
    PADDING_Y = 5

# Настройки дисплея
class DisplayConfig:
    BACKGROUND = ThemeConfig.BACKGROUND
    FOREGROUND = ThemeConfig.FOREGROUND
    JUSTIFY = "right"
    BORDER_WIDTH = 0

# Настройки звуков
class SoundConfig:
    ENABLED = True
    CLICK_SOUND = os.path.join("resources", "sounds", "click.wav")

# Конфигурация кнопок калькулятора
BUTTON_LAYOUT = [
    ("sin", 0, 0), ("cos", 0, 1), ("tan", 0, 2), ("C", 0, 3),
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("(", 4, 1), (")", 4, 2), ("+", 4, 3),
    ("=", 5, 0, 1, 4)
]

# Проверка существования ресурсов
def validate_resources():
    if not Path(FontConfig.FONT_PATH).exists():
        raise FileNotFoundError(f"Файл шрифта не найден: {FontConfig.FONT_PATH}")
    if not Path(IconConfig.ICON_PATH).exists():
        raise FileNotFoundError(f"Файл иконки не найден: {IconConfig.ICON_PATH}")
    if SoundConfig.ENABLED and not Path(SoundConfig.CLICK_SOUND).exists():
        print(f"⚠️ Файл звука не найден: {SoundConfig.CLICK_SOUND}")
        SoundConfig.ENABLED = False
