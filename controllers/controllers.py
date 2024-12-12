# -*- coding: utf-8 -*-
# from odoo import http


# class Estacion(http.Controller):
#     @http.route('/estacion/estacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estacion/estacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estacion.listing', {
#             'root': '/estacion/estacion',
#             'objects': http.request.env['estacion.estacion'].search([]),
#         })

#     @http.route('/estacion/estacion/objects/<model("estacion.estacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estacion.object', {
#             'object': obj
#         })

