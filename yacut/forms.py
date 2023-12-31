from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Optional


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Ссылка', validators=[DataRequired(message='Обязательное поле')])
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(), ])
    submit = SubmitField('Создать')