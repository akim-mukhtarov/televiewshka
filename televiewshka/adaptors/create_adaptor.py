from .base import AbstractBaseAdaptor
from .telebot_adaptor import TelebotAdaptor


_adaptors = {
    # <bot class name: str> : <adaptor class: Type>
    "TeleBot": TelebotAdaptor,
}


def create_adaptor(bot) -> AbstractBaseAdaptor:
    class_name = bot.__class__.__name__
    adaptor = _adaptors.get(class_name)
    if not adaptor:
        raise ValueError(
                f"{class_name} is not supported\n"
                f"Suppoted classes: {list(_adaptors.keys())}")
    return adaptor(bot)
