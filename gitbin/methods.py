"""همه متدهای API گیت‌بین — ۴۵ متد"""


class BotMethods:
    # ═══════════════ هویت و آپدیت ═══════════════

    def get_me(self):
        """اطلاعات ربات"""
        return self._call("getMe")

    def get_updates(self, offset=None, limit=None, timeout=None, allowed_updates=None):
        """دریافت آپدیت‌ها (long polling)"""
        return self._call("getUpdates", offset=offset, limit=limit,
                          timeout=timeout, allowed_updates=allowed_updates)

    def set_webhook(self, url, **kwargs):
        return self._call("setWebhook", url=url, **kwargs)

    def delete_webhook(self, **kwargs):
        return self._call("deleteWebhook", **kwargs)

    def get_webhook_info(self):
        return self._call("getWebhookInfo")

    def get_file(self, file_id):
        return self._call("getFile", file_id=file_id)

    # ═══════════════ دستورات و منو ═══════════════

    def set_my_commands(self, commands, **kwargs):
        """commands: [{"command": "start", "description": "شروع"}]"""
        return self._call("setMyCommands", commands=commands, **kwargs)

    def get_my_commands(self, **kwargs):
        return self._call("getMyCommands", **kwargs)

    def set_chat_menu_button(self, **kwargs):
        return self._call("setChatMenuButton", **kwargs)

    def get_chat_menu_button(self, **kwargs):
        return self._call("getChatMenuButton", **kwargs)

    def set_user_emoji_status(self, user_id, emoji_status_custom_emoji_id=None, **kwargs):
        return self._call("setUserEmojiStatus", user_id=user_id,
                          emoji_status_custom_emoji_id=emoji_status_custom_emoji_id, **kwargs)

    # ═══════════════ ارسال پیام ═══════════════

    def send_message(self, chat_id, text, **kwargs):
        return self._call("sendMessage", chat_id=chat_id, text=text, **kwargs)

    def send_photo(self, chat_id, photo, **kwargs):
        return self._call("sendPhoto", chat_id=chat_id, photo=photo, **kwargs)

    def send_audio(self, chat_id, audio, **kwargs):
        return self._call("sendAudio", chat_id=chat_id, audio=audio, **kwargs)

    def send_document(self, chat_id, document, **kwargs):
        return self._call("sendDocument", chat_id=chat_id, document=document, **kwargs)

    def send_video(self, chat_id, video, **kwargs):
        return self._call("sendVideo", chat_id=chat_id, video=video, **kwargs)

    def send_animation(self, chat_id, animation, **kwargs):
        return self._call("sendAnimation", chat_id=chat_id, animation=animation, **kwargs)

    def send_voice(self, chat_id, voice, **kwargs):
        return self._call("sendVoice", chat_id=chat_id, voice=voice, **kwargs)

    def send_video_note(self, chat_id, video_note, **kwargs):
        return self._call("sendVideoNote", chat_id=chat_id, video_note=video_note, **kwargs)

    def send_sticker(self, chat_id, sticker, **kwargs):
        return self._call("sendSticker", chat_id=chat_id, sticker=sticker, **kwargs)

    def send_dice(self, chat_id, emoji=None, **kwargs):
        """تاس/بسکتبال/فوتبال/... — emoji: 🎲 🎯 🎳 🏀 ⚽ 🎰"""
        return self._call("sendDice", chat_id=chat_id, emoji=emoji, **kwargs)

    # ─── سه متد ویژه: به‌جای chat_id، receiver_user_id لازم دارن ───
    def send_location(self, chat_id, receiver_user_id, latitude, longitude, **kwargs):
        return self._call("sendLocation", chat_id=chat_id, receiver_user_id=receiver_user_id,
                          latitude=latitude, longitude=longitude, **kwargs)

    def send_venue(self, chat_id, receiver_user_id, latitude, longitude, title, address, **kwargs):
        return self._call("sendVenue", chat_id=chat_id, receiver_user_id=receiver_user_id,
                          latitude=latitude, longitude=longitude,
                          title=title, address=address, **kwargs)

    def send_contact(self, chat_id, receiver_user_id, phone_number, first_name, **kwargs):
        return self._call("sendContact", chat_id=chat_id, receiver_user_id=receiver_user_id,
                          phone_number=phone_number, first_name=first_name, **kwargs)

    # ═══════════════ ویرایش و حذف ═══════════════

    def edit_message_text(self, chat_id, message_id, text, **kwargs):
        return self._call("editMessageText", chat_id=chat_id,
                          message_id=message_id, text=text, **kwargs)

    def delete_message(self, chat_id, message_id):
        return self._call("deleteMessage", chat_id=chat_id, message_id=message_id)

    def answer_callback_query(self, callback_query_id, text=None, show_alert=None, **kwargs):
        return self._call("answerCallbackQuery", callback_query_id=callback_query_id,
                          text=text, show_alert=show_alert, **kwargs)

    # ═══════════════ مدیریت چت ═══════════════

    def ban_chat_member(self, chat_id, user_id, **kwargs):
        return self._call("banChatMember", chat_id=chat_id, user_id=user_id, **kwargs)

    def unban_chat_member(self, chat_id, user_id, **kwargs):
        return self._call("unbanChatMember", chat_id=chat_id, user_id=user_id, **kwargs)

    def restrict_chat_member(self, chat_id, user_id, permissions=None, **kwargs):
        """permissions: dict مثل {"can_send_messages": False}"""
        return self._call("restrictChatMember", chat_id=chat_id, user_id=user_id,
                          permissions=permissions, **kwargs)

    def promote_chat_member(self, chat_id, user_id, **kwargs):
        return self._call("promoteChatMember", chat_id=chat_id, user_id=user_id, **kwargs)

    def pin_chat_message(self, chat_id, message_id, **kwargs):
        return self._call("pinChatMessage", chat_id=chat_id, message_id=message_id, **kwargs)

    def unpin_chat_message(self, chat_id, message_id=None, **kwargs):
        return self._call("unpinChatMessage", chat_id=chat_id, message_id=message_id, **kwargs)

    def get_chat_administrators(self, chat_id):
        return self._call("getChatAdministrators", chat_id=chat_id)

    def get_chat_member(self, chat_id, user_id):
        return self._call("getChatMember", chat_id=chat_id, user_id=user_id)

    # ═══════════════ استارز (قابلیت ویژه گیت‌بین) ═══════════════

    def get_my_star_balance(self):
        """موجودی استارز ربات"""
        return self._call("getMyStarBalance")

    def get_available_gifts(self):
        return self._call("getAvailableGifts")

    def send_gift(self, gift_id, **kwargs):
        return self._call("sendGift", gift_id=gift_id, **kwargs)

    def gift_premium_subscription(self, user_id, **kwargs):
        return self._call("giftPremiumSubscription", user_id=user_id, **kwargs)

    def refund_star_payment(self, user_id, telegram_payment_charge_id, **kwargs):
        return self._call("refundStarPayment", user_id=user_id,
                          telegram_payment_charge_id=telegram_payment_charge_id, **kwargs)

    def transfer_stars(self, user_id, amount, **kwargs):
        """انتقال استارز از کیف پول ربات به یک کاربر"""
        return self._call("transferStars", user_id=user_id, amount=amount, **kwargs)

    # ═══════════════ پرداخت ═══════════════

    def send_invoice(self, chat_id, title, description, payload,
                     provider_token, currency, prices, **kwargs):
        return self._call("sendInvoice", chat_id=chat_id, title=title,
                          description=description, payload=payload,
                          provider_token=provider_token, currency=currency,
                          prices=prices, **kwargs)

    def answer_pre_checkout_query(self, pre_checkout_query_id, ok, **kwargs):
        return self._call("answerPreCheckoutQuery",
                          pre_checkout_query_id=pre_checkout_query_id,
                          ok=ok, **kwargs)

    def answer_shipping_query(self, shipping_query_id, ok, **kwargs):
        """⚠️ در اسکن 404 داد — با احتیاط استفاده کن"""
        return self._call("answerShippingQuery",
                          shipping_query_id=shipping_query_id, ok=ok, **kwargs)

    # ═══════════════ WebApp ═══════════════

    def answer_web_app_query(self, web_app_query_id, result, **kwargs):
        return self._call("answerWebAppQuery",
                          web_app_query_id=web_app_query_id, result=result, **kwargs)

    def save_prepared_inline_message(self, user_id, result, **kwargs):
        return self._call("savePreparedInlineMessage",
                          user_id=user_id, result=result, **kwargs)