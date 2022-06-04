from .abstract_base_adaptor import AbstractBaseAdaptor


class TelebotAdaptor(AbstractBaseAdaptor):
    def __init__(self, bot: "TeleBot"):
        pass

    def send_message(self, message):
        pass

    def start(self):
        self.bot.start_polling()
