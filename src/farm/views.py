#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import api, app
from farm.database import db_session
from flask import render_template, request
from flask_restful import Resource, reqparse
from log import log
from business import fm

@app.errorhandler(Exception)
def special_exception_handler(error):
    log.error(error)
    return 'Internal Server Error', 500


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
@app.route('/index')
def index():
    return render_template("/index.html")

@app.route("/farm")
def farm():
    return render_template("farm/index.html")


class SeedResource(Resource):
    def get(self, name):
        return fm.get_seed_by_name(name).dic()

    def post(self, name):
        body = request.get_json()
        if "number" not in body:
            return "BadRequest", 400
        return fm.add_or_update(name, body).dic()

    def put(self, name):
        body = request.get_json()
        if "number" not in body:
            return "BadRequest", 400
        return fm.add_or_update(name, body).dic()

    def delete(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('del', type=int, location='args', default=0)
        args = parser.parse_args()

        if args["del"] == 1:
            return fm.delete_seed(name)
        else:
            return fm.disable_seed(name).dic()


class SeedListResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', type=int, location='args', default=10)
        parser.add_argument('del', type=int, location='args', default=0)
        args = parser.parse_args()
        if args["del"] == 1:
            return [s.dic() for s in fm.get_sell_list(args["limit"])]
        else:
            return [s.dic() for s in fm.get_top_seeds(args["limit"])]


class SeedAllResource(Resource):
    def get(self):
        return [s.dic() for s in fm.get_all_seeds()]

api.add_resource(SeedResource, "/api/farm/seed/<string:name>")
api.add_resource(SeedListResource, "/api/farm/seed/list")
api.add_resource(SeedAllResource, "/api/farm/seeds")
