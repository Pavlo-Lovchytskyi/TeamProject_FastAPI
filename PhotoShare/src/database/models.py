from sqlalchemy import Column, Integer, String, func, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship


Base = declarative_base()


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(15), unique=True)
    share_id = Column('shares_id', ForeignKey('shares.id', ondelete='CASCADE'), default=None)
    share = relationship('Share', backref='tags')


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    created_at = Column('crated_at', DateTime, default=func.now())
    updated_at = Column('updated_at', DateTime, default=func.now())
    share_id = Column('shares_id', ForeignKey('shares.id', ondelete='CASCADE'), default=None)
    user_id = Column('users_id', ForeignKey('users.id', ondelete='CASCADE'))
    share = relationship('Share', backref='comments')


class Share(Base):
    __tablename__ = 'shares'

    id = Column(Integer, primary_key=True, index=True)
    #name_share = Column(String, index=True, unique=True, nullable=False) # убрати unique= False
    image = Column(String, index=True, nullable=False) # назвати url
    qrcode = Column(String, index=True) # image_qr
    description = Column(String, index=True, nullable=False)
    created_at = Column('crated_at', DateTime, default=func.now())
    updated_at = Column('updated_at', DateTime, default=func.now())
    user_id = Column('users_id', ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship('User', backref='shares')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    created_at = Column('crated_at', DateTime, default=func.now())
    refresh_token = Column(String(255), nullable=True)
    role = Column(String, index=True, default='user')
    confirmed = Column(Boolean, default=False)
