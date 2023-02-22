"""Модуль содержит настройки obyebot, конфигурируемые через переменные окружения. """

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
