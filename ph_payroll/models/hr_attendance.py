from odoo import api, fields, models, tools

class PhAttendance(models.Model):
    _inherit = 'hr.attendance'
    
    ph_schedule = fields.Char()
    ph_work_from = fields.Char()
    ph_work_to = fields.Char()
    ph_absent = fields.Float()
    ph_late = fields.Float()
    ph_undertime = fields.Float()
    ph_on_leave = fields.Boolean()
    ph_overtime = fields.Float()
    ph_ot_permit = fields.Boolean()