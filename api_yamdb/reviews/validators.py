import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(year):
    if year > timezone.now().year:
        raise ValidationError(f'Год {year} больше текущего!')


def validate_username(username):
    if username.lower() in settings.RESERVED_USERNAMES:
        raise ValidationError(f'Имя пользователя не может быть {username}.')
    wrong_symbols = re.findall(settings.VALID_USERNAME, username)
    if wrong_symbols:
        set_wrong_symbols = set(''.join(wrong_symbols))
        str_wrong_symbols = ', '.join(set_wrong_symbols)
        raise ValidationError(
            f'Обнаружены недопустимые символы: {str_wrong_symbols}!')
