from typing import Optional, Iterable


class Button:
    def __init__(text: str, on_click: str):
        self.text=text
        self.on_click=on_click


class KeyboardLayout:
    def __init__(self, text: Optional[str] = "", keyboard: Iteralbe[Iterable[Button]]):
        self.text=text
        self.keyboard=keyboard
