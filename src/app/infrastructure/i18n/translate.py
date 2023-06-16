import os
from pyi18n import PyI18n
from pyi18n.loaders import PyI18nYamlLoader
from src.app.domain.i18n.translate_service import TranslateService

root_path_i18n = os.path.dirname(os.path.abspath(__file__))


class Translate(TranslateService):
    DEFAULT_LOCALE = "es"

    def __init__(self, locale: str = DEFAULT_LOCALE):
        self.default_locale = locale
        loader_path: PyI18nYamlLoader = PyI18nYamlLoader(f'{root_path_i18n}/locales/')
        available_locales = ('es', 'en')
        self.i18n: PyI18n = PyI18n(available_locales, loader=loader_path)

    def text(self, text: str, **kwargs) -> str:
        return self.i18n.gettext(self.default_locale, text, **kwargs)
