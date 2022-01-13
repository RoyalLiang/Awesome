from sqlalchemy import Column, String, SmallInteger

from app.utils.base import BaseModel


class LabelModel(BaseModel):
    __tablename__ = 'liang_label'

    name = Column(String(50), index=True, comment='名称')
    desc = Column(String(150), nullable=True, default='', comment='描述')
    cat = Column(SmallInteger(), comment='1:tag,2:category')
