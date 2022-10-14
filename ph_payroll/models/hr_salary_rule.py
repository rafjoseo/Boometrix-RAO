from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval

class PhSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'
    
    taxable = fields.Boolean()
    sss_contribution = fields.Boolean()
    philhealth_contribution = fields.Boolean()
    pagibig_contribution = fields.Boolean()
    
    def _compute_rule(self, localdict):

        """
        :param localdict: dictionary containing the current computation environment
        :return: returns a tuple (amount, qty, rate)
        :rtype: (float, float, float)
        """
        self.ensure_one()
        if self.amount_select == 'fix':
            try:
                return self.amount_fix or 0.0, float(safe_eval(self.quantity, localdict)), 100.0
            except Exception as e:
                self._raise_error(localdict, _("Wrong quantity defined for:"), e)
        if self.amount_select == 'percentage':
            try:
                return (float(safe_eval(self.amount_percentage_base, localdict)),
                        float(safe_eval(self.quantity, localdict)),
                        self.amount_percentage or 0.0)
            except Exception as e:
                self._raise_error(localdict, _("Wrong percentage base or quantity defined for:"), e)
        else:  # python code
            try:
                safe_eval(self.amount_python_compute or 0.0, localdict, mode='exec', nocopy=True)
                # rate for bi-monthly schedule_pay
                rate = self.amount_percentage if self.struct_id.schedule_pay == 'bi-monthly' else localdict.get('result_rate', 100.0)
                
                return float(localdict['result']), localdict.get('result_qty', 1.0), rate or 0.0
            except Exception as e:
                self._raise_error(localdict, _("Wrong python code defined for:"), e)
    