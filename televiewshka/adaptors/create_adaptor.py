from .base import AbstractBaseAdaptor
from .telebot_adaptor import TelebotAdaptor


_adaptors = {
    # <bot class name: str> : <adaptor class: Type>
    "TeleBot": TelebotAdaptor,
}


def create_adaptor(bot) -> AbstractBaseAdaptor:
    # adaptor = _adaptors.get(bot.__class__.__name__)
    # if not adaptor:
    #       raise
    # return adaptor.__init__(bot)
    pass
