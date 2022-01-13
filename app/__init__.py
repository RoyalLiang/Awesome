
# from dotenv import load_dotenv
from flask import Flask

from loguru import logger

from app.utils.db import db

logger.add(sink=f"../logs/blog.log", rotation='00:00', enqueue=True)


def register_blueprints(app):
    from app.api.v1 import create_v1

    app.register_blueprint(create_v1(), url_prefix="/v1")


def apply_cors(app):
    from flask_cors import CORS
    CORS(app)


def load_app_config(app):
    """
    根据指定配置环境自动加载对应环境变量和配置类到app config
    """
    # 根据传入环境加载对应配置
    # env = app.config.get("ENV")
    env = 'dev'
    # 读取 .env
    # load_dotenv(".{env}.env".format(env=env))
    # 读取配置类
    app.config.from_object(
        "app.config.{env}".format(env=env)
    )


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app(register_all=True, **kwargs):
    # load_dotenv(".flaskenv")
    app = Flask(__name__, static_folder="../assets")
    load_app_config(app)
    if register_all:
        register_blueprints(app)
        apply_cors(app)
    db.init_app(app)
    return app
