# -*- coding: utf-8 -*-
from odoo import http


class Base11(http.Controller):
    @http.route('/base_11/base_11', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/base_11/base_11/objects', auth='public')
    def list(self, **kw):
        return http.request.render('base_11.listing', {
            'root': '/base_11/base_11',
            'objects': http.request.env['base_11.base_11'].search([]),
        })

    @http.route('/base_11/base_11/objects/<model("base_11.base_11"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('base_11.object', {
            'object': obj
        })
