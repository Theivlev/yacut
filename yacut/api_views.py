from http import HTTPStatus

from flask import jsonify, request

from yacut.validators import validate_data

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify(url=url.original), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_short_link():
    data = request.get_json()
    validate_data(data)
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        short_link='http://localhost/' + url_map.short,
        url=url_map.original), HTTPStatus.CREATED