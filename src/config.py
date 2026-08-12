"""Deployment configuration for Confederate bridge."""
import os

from env_loader import load_env
load_env()

DISCORD_TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")

ADMINS = {
    "discord": set(),
    "telegram": set()
}

SERVICE_CHATS = {
    "discord": set(),
    "telegram": set(),
}

BACKUP_CHATS = {
    "discord": set(),
    "telegram": set(),
}

GALLERY = set()

SUPPORT_CHATS = {
    "discord": set(),
    "telegram": set(),
}

VERIFIED = set()
UNVERIFIED = set()

PURGATORIUM_GUILD_ID = 0
PURGATORIUM_INVITE_URL = ""
GUARD_BOT_ID = 0
APPEAL_CHANNEL_ID = 0

APPEAL_PARDON_CHANNELS = {
    "discord": set(),
}

APPEAL_BANINFO_CHANNELS = {
    "discord": set(),
}

CONSULS = set()

WIKI_CONTACT = "https://github.com/HIHRAIM/Confederate"
