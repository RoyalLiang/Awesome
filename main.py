import traceback

import loguru
from flask import jsonify

from app import create_app
from app.utils.db import db
from app.utils.errors import JsonError

app = create_app()
logger = loguru.logger

with app.app_context():
    # from app.models.article import ArticleModel, ArticleLabelModel
    # from app.models.label import LabelModel
    from app.models import *
    db.create_all()


@app.errorhandler(Exception)
def framework_error(e):
    r = dict(result=-1, msg=None)
    logger.error(f'error, msg: {traceback.format_exc()}')
    if isinstance(e, JsonError):
        r['msg'] = e.message
    else:
        r['msg'] = str(e)
    return jsonify(r)


if __name__ == '__main__':
    app.run()
