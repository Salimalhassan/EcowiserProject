# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.authentication.models import *
from datetime import date, datetime, timedelta
from hashlib import sha256
from pyexpat.errors import XML_ERROR_INCOMPLETE_PE
from typing import ItemsView
from flask import Blueprint , flash, make_response, render_template, url_for, redirect, jsonify , request
from pkg_resources import DefaultProvider
from apps import db

import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user,LoginManager
from sqlalchemy import desc,select

@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')

@blueprint.route('/recipelist',methods=['GET','POST'])
@login_required
def recipelist():
    recipes= Recipe.query.all()
    return render_template('home/tbl_bootstrap.html', segment='index',recipes=recipes)

@blueprint.route('/addrecipe',methods=['GET', 'POST'])
@login_required
def Addrecipe():
       
       if request.method == 'POST' :   
           alla=request.get_json('items')
           print(alla)
           xl = alla["items"]
           xl2 = alla["items2"]
           xl3 = alla["items3"]
           xl4 = alla["items4"]
           xl5 = alla["items5"]
           xl6 = alla["items6"]
           newrecipe= Recipe(recipe_title=xl,user_id = current_user.id,meal=xl2,cuisine=xl3,ingredients=xl4,description=xl5,directions=xl6)
           db.session.add(newrecipe)
           db.session.commit()  
           res = make_response(jsonify({'quantity':alla}),200)
           
       return render_template('home/form_elements.html',segment='addrecipe')   
       

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500
    

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
