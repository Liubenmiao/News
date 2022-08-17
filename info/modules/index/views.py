#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Author:       LBM
Date:         2022/8/17
Name:         views
Description:  
"""

from . import index_blu


@index_blu.route('/')
def index():
    return 'Welcome to the News'
