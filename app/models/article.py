from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship, lazyload

from app.utils.base import BaseModel
from app.utils.db import db


class ArticleModel(BaseModel):
    __tablename__ = 'liang_article'

    title = Column(String(50), index=True, comment='标题')
    cat = relationship('LabelModel', secondary='liang_article_label', backref=db.backref('articles', lazy='dynamic'), lazy='dynamic')
    author = Column(String(50), comment='作者')
    summary = Column(String(200), nullable=True, comment='简介')
    cover = Column(String(50), nullable=True, comment='封面图')
    content = Column(Text(), comment='内容')
    comments = Column(Integer(), default=0, comment='评论数')
    likes = Column(Integer(), default=0, comment='点赞数')


class ArticleLabelModel(db.Model):
    __tablename__ = 'liang_article_label'

    id = Column(Integer, primary_key=True, autoincrement=True)
    article = Column(Integer, ForeignKey('liang_article.id'))
    label = Column(Integer, ForeignKey('liang_label.id'))


