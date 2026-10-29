from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class LightButton(Button):
    def render(self) -> None:
        print("Rendu d'un bouton BLANC avec texte noir.")


class LightCheckbox(Checkbox):
    def render(self) -> None:
        print("Rendu d'une case à cocher CLAIRE.")


class DarkButton(Button):
    def render(self) -> None:
        print("Rendu d'un bouton NOIR avec texte blanc.")


class DarkCheckbox(Checkbox):
    def render(self) -> None:
        print("Rendu d'une case à cocher SOMBRE.")


class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class LightThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


class Application:
    def init(self, factory: UIFactory) -> None:
        self._button = factory.create_button()
        self._checkbox = factory.create_checkbox()

    def render_ui(self) -> None:
        self._button.render()
        self._checkbox.render()


current_theme = "Dark"

if current_theme == "Dark":
    factory = DarkThemeFactory()
else:
    factory = LightThemeFactory()

app = Application(factory)
app.render_ui()