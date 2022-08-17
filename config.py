#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Author:       LBM
Date:         2022/8/17
Name:         config
Description:  
"""

import redis


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
    REDIS_HOST = '192.168.2.6'
    REDIS_PORT = 6379

    # felsk_session配置
    SESSION_TYPE = 'redis'  # 指定session保存在到redis中
    SESSION_USE_SIGNER = True  # cookie中的session_id被加密处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


class DevelopementConfig(Config):
    """开发模式下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产模式下的配置"""
    pass


config = {
    "development": DevelopementConfig,
    "production": ProductionConfig
}
