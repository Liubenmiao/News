#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Author:       LBM
Date:         2022/8/17
Name:         __init__.py
Description:  
"""

from flask import Blueprint

index_blu = Blueprint("index", __name__)

from . import views
