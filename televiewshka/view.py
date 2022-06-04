from abc import ABC, abstractmethod
from .layouts import KeyboardLayout
from .adaptors.base import Message


class AbstractBaseView(ABC):
    def __init__(self, user):
        self.user = user


class KeyboardView(AbstractBaseView):
    @staticmethod
    @abstractmethod
    def render(*args, **kwargs) -> KeyboardLayout:
        pass


class TextView(AbstractBaseView):
    @staticmethod
    @abstractmethod
    def render(*args, **kwargs) -> str:
        pass


class TextDialogView(TextView):
    @abstractmethod
    def on_message(self, message: Message):
        pass
