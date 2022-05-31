# Televiewshka

> Note: as for now, this is neither stable nor working code.
Being Created in ... purposes it is a subject for further updates and improvements

_viewshka_ - Russian noun: informal of eng. "view", obtained by adding a diminutive suffix "shka"

Televiewshka allows you develop UI & logic for telegram bots with class based views.
In views you can define its content and how user actions and replies must be handled on it.
When all stuff related particular step in user flow is held in one class, you can clearly
see relationship between components

## (Supposed) Example

```py
from televiewshka import KeyboardView, KeyboardLayout, button, render


class FirstView(KeyboardView):
    def next(self):
        return render("NextView", inplace=True, param=42)

    @classmethod
    def render(cls):
        return KeyboardLayout(button("Go next", on_click="next"))


class NextView(KeyboardView):
    def back(self):
        return render(FirstView, inplace=True)

    @classmethod
    def render(cls, param):
        return KeyboardLayout(
            text=f"Passed param: {param}",
            button("Go back", on_click="back"))
```

## Some details explained

### Views

something that can be rendered to user
and than handle user actions on itselves
actions are dispatched to appropriate view' and method
in accordance with user state (e.g. current_scene flag)
which is set when the view is rendered

### Dispatch

messages are being dispatched according to user' state
state = current view
callback data or message = view method

### User state

pass
