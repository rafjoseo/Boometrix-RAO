from odoo import api, fields, models, _


class PhEmployee(models.Model):
    _inherit = 'hr.employee'
    
    ph_working_days = fields.Float(string="Working days in a year", required=True,)