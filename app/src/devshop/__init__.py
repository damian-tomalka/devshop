import logging
import os
import sys

from flask import Flask

from .models import db


def _database_url() -> str:
    url = os.environ.get("DATABASE_URL", "sqlite:///devshop.db")
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg://", 1)
    return url


def create_app(config: dict | None = None) -> Flask:
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = _database_url()
    app.config["APP_ENV"] = os.environ.get("APP_ENV", "development")
    if config:
        app.config.update(config)

    db.init_app(app)

    from .routes import bp

    app.register_blueprint(bp)

    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        app.logger.info("tabele utworzone")

    return app
