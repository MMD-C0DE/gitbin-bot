"""خطاهای API گیت‌بین"""


class GitbinError(Exception):
    """خطای پایه همه خطاهای گیت‌بین"""
    def __init__(self, code: int, description: str, method: str = ""):
        self.code = code
        self.description = description
        self.method = method
        msg = f"[{code}] {description}"
        if method:
            msg += f" (در متد {method})"
        super().__init__(msg)


# نقشه: description → اسم کلاس Exception
_ERROR_NAMES = {
    # احراز هویت
    "ACCESS_TOKEN_INVALID": "AccessTokenInvalid",

    # پارامترهای نامعتبر
    "CHAT_ID_INVALID": "ChatIdInvalid",
    "USER_ID_INVALID": "UserIdInvalid",
    "FILE_ID_INVALID": "FileIdInvalid",
    "GIFT_ID_INVALID": "GiftIdInvalid",
    "QUERY_ID_INVALID": "QueryIdInvalid",
    "BUTTON_INVALID": "ButtonInvalid",
    "BOT_COMMAND_INVALID": "BotCommandInvalid",
    "WEBHOOK_URL_INVALID": "WebhookUrlInvalid",
    "EMOTICON_INVALID": "EmoticonInvalid",
    "BOT_INVALID": "BotInvalid",

    # محدودیت‌ها
    "EPHEMERAL_TARGET_REQUIRED": "EphemeralTargetRequired",
    "FILE_TOO_BIG": "FileTooBig",

    # استارز
    "STARS_AMOUNT_INVALID": "StarsAmountInvalid",
    "BALANCE_TOO_LOW": "BalanceTooLow",
    "USER_NOT_FOUND": "UserNotFound",
    "USER_IS_BOT": "UserIsBot",

    # عمومی
    "METHOD_NOT_FOUND": "MethodNotFound",
    "CONFLICT": "ConflictError",
}

# ساخت پویا کلاس‌ها
import sys as _sys
_module = _sys.modules[__name__]
for _desc, _cls_name in _ERROR_NAMES.items():
    globals()[_cls_name] = type(_cls_name, (GitbinError,), {})


def raise_from_response(data: dict, method: str = ""):
    """از پاسخ خطای API، Exception مناسب بساز و raise کن"""
    desc = data.get("description", "UNKNOWN_ERROR")
    code = data.get("error_code", 0)
    cls_name = _ERROR_NAMES.get(desc, "GitbinError")
    cls = globals().get(cls_name, GitbinError)
    raise cls(code, desc, method)