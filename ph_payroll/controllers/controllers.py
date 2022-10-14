# -*- coding: utf-8 -*-
# from odoo import http


# class PhPayroll(http.Controller):
#     @http.route('/ph_payroll/ph_payroll', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ph_payroll/ph_payroll/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ph_payroll.listing', {
#             'root': '/ph_payroll/ph_payroll',
#             'objects': http.request.env['ph_payroll.ph_payroll'].search([]),
#         })

#     @http.route('/ph_payroll/ph_payroll/objects/<model("ph_payroll.ph_payroll"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ph_payroll.object', {
#             'object': obj
#         })
