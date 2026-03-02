#!/bin/env python3

import sqlalchemy
import sqlalchemy.orm

Base = sqlalchemy.orm.declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)

    username = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    password = sqlalchemy.Column(sqlalchemy.String)

    role = sqlalchemy.Column(sqlalchemy.String, default='user')

    totp_enabled = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    totp_verified = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    totp_key = sqlalchemy.Column(sqlalchemy.String)

    email = sqlalchemy.Column(sqlalchemy.String)

class Wireguard(Base):
    __tablename__ = 'wireguard_interfaces'