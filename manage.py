#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Author:       LBM
Date:         2022/7/25
Name:         manage
Description:  
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to the News'


if __name__ == '__main__':
    app.run()
