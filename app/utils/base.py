from datetime import datetime

from flask import jsonify
from sqlalchemy import Column, Integer, DateTime, SmallInteger

from app.utils.db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer(), primary_key=True, autoincrement=True, comment='主键')
    create_time = Column(DateTime(), default=datetime.now(), comment='创建时间')
    update_time = Column(DateTime(), nullable=True, comment='更新时间')
    status = Column(SmallInteger(), nullable=False, index=True, comment='状态')

    # 查
    @classmethod
    def get(cls, start=None, count=None, one=True, **kwargs):
        # 应用软删除，必须带有delete_time
        if kwargs.get("delete_time") is None:
            kwargs["delete_time"] = None
        if one:
            return cls.query.filter().filter_by(**kwargs).first()
        return cls.query.filter().filter_by(**kwargs).offset(start).limit(count).all()

    # 增
    @classmethod
    def create(cls, **kwargs):
        one = cls()
        for key in kwargs.keys():
            if hasattr(one, key):
                setattr(one, key, kwargs[key])
        db.session.add(one)
        if kwargs.get("commit") is True:
            db.session.commit()
        return one

    def update(self, **kwargs):
        for key in kwargs.keys():
            if hasattr(self, key) and key not in ['id']:
                setattr(self, key, kwargs[key])
        db.session.add(self)
        if kwargs.get("commit") is True:
            db.session.commit()
        return self


def json_response(result=0,  data=None, msg='success'):
    r = dict(result=result, data=data, msg=msg)
    return jsonify(r)
