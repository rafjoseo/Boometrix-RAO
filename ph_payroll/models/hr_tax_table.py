from odoo import api, fields, models, tools


class PhTaxTable(models.Model):
    _name = 'ph.tax.table'
    _description = "Tax Table"
    
    sequence = fields.Integer('Sequence', default=10)
    category = fields.Selection([('monthly', 'Monthly'),('semi_monthly', 'Semi-Monthly'),('annualize', 'Annualize')])
    floor = fields.Float()
    ceiling = fields.Float()
    absolute = fields.Float()
    rate = fields.Float()
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, required=True)
    
    
class PhSSSTable(models.Model):
    _name = 'ph.sss.table'
    _description = "SSS Contribution Table"
    
    sequence = fields.Integer('Sequence', default=10)
    salary_from = fields.Float()
    salary_to = fields.Float()
    salary_credit = fields.Float()
    sss_ee = fields.Float()
    sss_er = fields.Float()
    ec_er = fields.Float()
    wisp_ee = fields.Float()
    wisp_er = fields.Float()
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, required=True)
    
    
class PhPhilhealthTable(models.Model):
    _name = 'ph.philhealth.table'
    _description = "Philhealth Contribution Table"
    
    sequence = fields.Integer('Sequence', default=10)
    year = fields.Char()
    salary_from = fields.Float()
    salary_to = fields.Float()
    category = fields.Selection([('rate', 'Rate'),('amount', 'Amount')])
    premium = fields.Float()
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, required=True)