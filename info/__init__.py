#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Author:       LBM
Date:         2022/8/17
Name:         __init__.py
Description:  
"""

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config

db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    app = Flask(__name__)
    # 配置
    app.config.from_object(config[config_name])
    # 配置数据库
    db.init_app(app)
    # 配置redis
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启csrf保护
    CSRFProtect(app)
    # 设置session保存位置
    Session(app)

    # 注册蓝图
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    return app
