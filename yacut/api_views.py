from re import match

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify(url=url.original), 200


@app.route('/api/id/', methods=['POST'])
def add_short_link():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' not in data or data['custom_id'] == '' or data['custom_id'] is None:
        data['custom_id'] = get_unique_short_id()
    if len(data['custom_id']) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', 400)
    elif URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
    elif not match(r'^[A-Za-z0-9_]+$', data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(short_link='http://localhost/' + url_map.short, url=url_map.original), 201