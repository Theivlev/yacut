

import random
import string

from flask import abort, flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id(length=6):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    unique_id = ''.join(random.choice(chars) for i in range(length))
    if URLMap.query.filter_by(short=unique_id).first():
        get_unique_short_id()
    return unique_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short_link = form.custom_id.data
        if URLMap.query.filter_by(short=short_link).first():
            flash(f'Имя {short_link} уже занято!')
            form.custom_id.data = None
            return render_template('index.html', form=form)
        if not short_link:
            form.custom_id.data = get_unique_short_id()
        if len(form.custom_id.data) > 16:
            flash('Указано недопустимое имя для короткой ссылки')
            form.custom_id.data = None
            return render_template('index.html', form=form)
        url = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        db.session.add(url)
        db.session.commit()
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirection_view(short):
    url = URLMap.query.filter_by(short=short).first()
    if url is not None:
        original_link = url.original
        return redirect(original_link)
    abort(404)