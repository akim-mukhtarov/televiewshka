from abc import ABC, abstractmethod


class Message:
    pass


class Query:
    pass


class AbstractBaseAdaptor(ABC):

    def handler(self):
        pass

    def _handle_message(self, message: Message):
        pass

    def _handle_query(self, query: Query):
        pass

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def start(self):
        pass
