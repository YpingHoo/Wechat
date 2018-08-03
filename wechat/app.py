from flask import Flask
from models import db
import logging
from logging.handlers import RotatingFileHandler
from views_service import service_blueprint


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    logging.basicConfig(level=logging.DEBUG)
    file_log_handle = RotatingFileHandler(config.BASE_DIR + '/logs/wechat.log', maxBytes=1024 * 1024 * 100,
                                          backupCount=10)
    formatter = logging.Formatter('%(levelname)s %(filename)s : %(lineno)d %(message)s')
    file_log_handle.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handle)
    app.logger = logging

    app.register_blueprint(service_blueprint)

    return app
