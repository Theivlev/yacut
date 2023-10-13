from http import HTTPStatus
from re import match

from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id

DEFAULT_LENGTH = 6
MAX_LENGTH_LINK = 16


def validate_data(data):
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' not in data or \
            (data['custom_id'] == '') or \
            (data['custom_id'] is None):
        data['custom_id'] = get_unique_short_id(DEFAULT_LENGTH)
    if len(data['custom_id']) > MAX_LENGTH_LINK:
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки',
            HTTPStatus.BAD_REQUEST
        )
    elif URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.')
    elif not match(r'^[A-Za-z0-9_]+$', data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
