
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
import models
engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True,echo=True)
# 创建数据库引擎( 当前目录下保存数据库文件)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import User,Post
    Base.metadata.create_all(bind=engine)