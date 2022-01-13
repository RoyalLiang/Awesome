from flask import Blueprint

from app.api.v1 import article
from app.api.v1 import label


def create_v1():
    bp_v1 = Blueprint("v1", __name__)
    article.article_api.register(bp_v1)
    label.label_api.register(bp_v1)
    return bp_v1
