#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Author:       LBM
Date:         2022/7/25
Name:         manage
Description:  
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

# 创建 app，并传入配置模式：development / production
app = create_app('development')
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
