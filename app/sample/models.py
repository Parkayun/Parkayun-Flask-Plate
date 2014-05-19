# -*- coding:utf-8 -*-
import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey

from .. import Base


class SampleModel(Base):
    __tablename__ = 'sample'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())