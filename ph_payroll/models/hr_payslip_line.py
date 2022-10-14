from odoo import api, fields, models, tools

class PhPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'
    
    salary_rule_taxable = fields.Boolean(related='salary_rule_id.taxable', readonly=True)