"""کتابخانه گیت‌بین — Bot API"""
from .client import GitbinClient
from .methods import BotMethods
from .errors import GitbinError


class Bot(GitbinClient, BotMethods):
    """
    کلاس اصلی — همه ۴۵ متد + ارتباط با API

    مثال:
        from gitbin import Bot
        bot = Bot(token="1780243415:K0WZ...")
        bot.send_message(chat_id=123, text="سلام")
    """
    pass


__all__ = ["Bot", "GitbinError"]
__version__ = "1.0.0"