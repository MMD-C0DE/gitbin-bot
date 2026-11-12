"""انواع داده API گیت‌بین — بر اساس مستندات"""
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any


@dataclass
class User:
    id: int
    is_bot: bool = False
    first_name: str = ""
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None

    @classmethod
    def from_dict(cls, d: dict) -> "User":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


@dataclass
class Chat:
    id: int
    type: str = "private"          # private | group | supergroup | channel
    title: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    @classmethod
    def from_dict(cls, d: dict) -> "Chat":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


@dataclass
class Dice:
    emoji: str = "🎲"
    value: int = 0

    @classmethod
    def from_dict(cls, d: dict) -> "Dice":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


@dataclass
class Message:
    message_id: int
    date: int = 0
    text: Optional[str] = None
    caption: Optional[str] = None
    from_user: Optional[User] = None       # فیلد اصلی API: from
    chat: Optional[Chat] = None
    dice: Optional[Dice] = None
    photo: Optional[List[Dict[str, Any]]] = None
    document: Optional[Dict[str, Any]] = None
    video: Optional[Dict[str, Any]] = None
    audio: Optional[Dict[str, Any]] = None
    voice: Optional[Dict[str, Any]] = None
    sticker: Optional[Dict[str, Any]] = None
    animation: Optional[Dict[str, Any]] = None
    reply_to_message: Optional["Message"] = None
    successful_payment: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, d: dict) -> "Message":
        d = dict(d)
        if "from" in d:
            d["from_user"] = d.pop("from")
        if d.get("from_user"):
            d["from_user"] = User.from_dict(d["from_user"])
        if d.get("chat"):
            d["chat"] = Chat.from_dict(d["chat"])
        if d.get("dice"):
            d["dice"] = Dice.from_dict(d["dice"])
        if d.get("reply_to_message"):
            d["reply_to_message"] = Message.from_dict(d["reply_to_message"])
        allowed = {k: v for k, v in d.items() if k in cls.__dataclass_fields__}
        return cls(**allowed)


@dataclass
class CallbackQuery:
    id: str
    from_user: Optional[User] = None
    message: Optional[Message] = None
    data: Optional[str] = None

    @classmethod
    def from_dict(cls, d: dict) -> "CallbackQuery":
        d = dict(d)
        if "from" in d:
            d["from_user"] = d.pop("from")
        if d.get("from_user"):
            d["from_user"] = User.from_dict(d["from_user"])
        if d.get("message"):
            d["message"] = Message.from_dict(d["message"])
        allowed = {k: v for k, v in d.items() if k in cls.__dataclass_fields__}
        return cls(**allowed)


@dataclass
class Update:
    update_id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    callback_query: Optional[CallbackQuery] = None

    @classmethod
    def from_dict(cls, d: dict) -> "Update":
        d = dict(d)
        if d.get("message"):
            d["message"] = Message.from_dict(d["message"])
        if d.get("edited_message"):
            d["edited_message"] = Message.from_dict(d["edited_message"])
        if d.get("callback_query"):
            d["callback_query"] = CallbackQuery.from_dict(d["callback_query"])
        return cls(**d)


@dataclass
class StarBalance:
    amount: int = 0
    nanostar_amount: int = 0

    @classmethod
    def from_dict(cls, d: dict) -> "StarBalance":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})