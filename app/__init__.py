# -*- coding:utf-8 -*-
from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)

engine = create_engine('db_path', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def create_app():

    from sample import sample_blueprint
    app.register_blueprint(sample_blueprint)

    return app