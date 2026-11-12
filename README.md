# gitbin-bot

کتابخانه پایتون برای GitBin Bot API.

## نصب

```bash
pip install gitbin-bot
```

## استفاده

```python
from gitbin import Bot

bot = Bot(token="YOUR_TOKEN")

# اطلاعات ربات
me = bot.get_me()
print(me["first_name"])

# ارسال پیام
bot.send_message(chat_id=123, text="سلام 👋")

# موجودی استارز
bal = bot.get_my_star_balance()
print(f"{bal['amount']:,} استارز")
```

## متدهای موجود

getMe, getUpdates, sendMessage, sendPhoto, sendDocument, sendVideo, sendAudio, sendVoice, sendAnimation, sendVideoNote, sendSticker, sendDice, sendLocation, sendVenue, sendContact, editMessageText, deleteMessage, answerCallbackQuery, banChatMember, unbanChatMember, restrictChatMember, promoteChatMember, pinChatMessage, unpinChatMessage, getChatAdministrators, getChatMember, setMyCommands, getMyCommands, setChatMenuButton, getChatMenuButton, getFile, setWebhook, deleteWebhook, getWebhookInfo, getMyStarBalance, transferStars, sendGift, giftPremiumSubscription, getAvailableGifts, refundStarPayment, sendInvoice, answerPreCheckoutQuery, answerShippingQuery, answerWebAppQuery, savePreparedInlineMessage, setUserEmojiStatus

**جمعاً ۴۵ متد.**

## لایسنس

MIT