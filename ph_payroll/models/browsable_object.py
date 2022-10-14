from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import fields

class BrowsableObject(object):
    def __init__(self, employee_id, dict, env):
        self.employee_id = employee_id
        self.dict = dict
        self.env = env

    def __getattr__(self, attr):
        return attr in self.dict and self.dict.__getitem__(attr) or 0.0

    def __getitem__(self, key):
        return self.dict[key] or 0.0
    

class PhPayslips(BrowsableObject):
    """a class that will be used into the python code, mainly for usability purposes"""

    def sum(self, code, month, year):
        self.env.cr.execute("""
            SELECT sum(pl.total)
            FROM hr_payslip as hp, hr_payslip_line as pl
            WHERE hp.employee_id = %s
            AND hp.state = 'done'
            AND hp.month = %s
            AND hp.year = %s
            AND hp.id = pl.slip_id
            AND pl.code = %s""", (self.employee_id, month, year, code))
        res = self.env.cr.fetchone()
        return res and res[0] or 0.0