#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Author:       LBM
Date:         2022/7/25
Name:         manage
Description:  
"""

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


class Config(object):
    """项目配置信息"""
    DEBUG = True
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    # mysql数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flask_test'
    SQLALCHEMY_ECHO = True  # 查询时会显示原始SQL语句
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 进行增删改查的时候设置是否立即提交的配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 动态追踪修改设置，如未设置只会提示警告

    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # felsk_session配置
    # SESSION_TYPE = 'redis'  # 指定session保存在到redis中
    SESSION_USE_SIGNER = True  # cookie中的session_id被加密处理
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


app.config.from_object(Config)
db = SQLAlchemy(app)
# redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
CSRFProtect(app)
Session(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    return 'Welcome to the News'


if __name__ == '__main__':
    manager.run()
