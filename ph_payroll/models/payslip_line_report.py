# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools


class PhPayslipLineReport(models.Model):
    _name = 'ph.payslip.line.report'
    _description = 'Payslip Line Report'
    _auto = False

    employee_id = fields.Many2one('hr.employee', string="Employee", readonly=True)
    payslip_id = fields.Many2one('hr.payslip', string="Payslip Name", readonly=True)
    payslip_line = fields.Many2one('hr.payslip.line', string="Payslip Line", readonly=True)
    payslip_start_date = fields.Date(readonly=True)
    payslip_end_date = fields.Date(readonly=True)
    company_id = fields.Many2one('res.company', readonly=True)
    payslip_amount = fields.Float(string="Amount", readonly=True)
    payslip_total_amount = fields.Float(string="Total", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
             CREATE or REPLACE view %s as (
                SELECT
                    row_number() OVER(PARTITION BY p.employee_id, pl.id) AS id,
                    pl.id as payslip_line,
                    pl.slip_id AS payslip_id,
                    p.employee_id,
                    p.company_id,
                    p.date_from as payslip_start_date,
                    p.date_to as payslip_end_date,
                    pl.amount AS payslip_amount,
                    pl.total AS payslip_total_amount
                FROM hr_payslip_line pl
                LEFT JOIN hr_payslip p on (p.id = pl.slip_id)
                WHERE p.state = 'paid'
            );
        """ % self._table)

