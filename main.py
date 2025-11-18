import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, 
    ContextTypes, MessageHandler, filters
)
import sqlite3
from datetime import datetime, timedelta
import random
import json
import asyncio

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Конфигурация
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
DATABASE_NAME = "english_learning.db"

# Категории слов по умолчанию
DEFAULT_CATEGORIES = [
    "basic", "food", "animals", "family", "colors", 
    "numbers", "verbs", "adjectives", "professions", "travel"
]
