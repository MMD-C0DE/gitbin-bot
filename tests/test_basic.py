"""تست ساده کتابخانه"""
import os
from gitbin import Bot

TOKEN = os.environ.get("GITBIN_TOKEN", "")


def test_import():
    """کتابخانه نصب شده"""
    from gitbin import Bot
    assert Bot is not None


def test_get_me():
    """اتصال به API"""
    if not TOKEN:
        return  # اگه توکن نداری، رد شو
    bot = Bot(token=TOKEN)
    me = bot.get_me()
    assert me["is_bot"] is True