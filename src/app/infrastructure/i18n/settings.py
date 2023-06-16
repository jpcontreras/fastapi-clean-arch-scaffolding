from pyi18n import PyI18n
from pyi18n.loaders import PyI18nYamlLoader
from main import root_path

loader_path: PyI18nYamlLoader = PyI18nYamlLoader(f'{root_path}/src/app/infrastructure/i18n/locales/')
available_locales = ('es', 'en')
i18n: PyI18n = PyI18n(available_locales, loader=loader_path)
DEFAULT_LOCALE = "es"
translate = i18n.gettext
