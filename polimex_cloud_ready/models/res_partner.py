from odoo import api, fields, models, tools, SUPERUSER_ID, _

class Partner(models.Model):
    _inherit = ['res.partner']

    company_id = fields.Many2one('res.company',
                                 readonly=True,
                                 default=lambda self: self.env.company)

    @api.depends('user_ids.share', 'user_ids.active')
    def _compute_partner_share(self):
        self.partner_share = False
        # super_partner = self.env['res.users'].browse(SUPERUSER_ID).partner_id
        # if super_partner in self:
        #     super_partner.partner_share = False
        # for partner in self - super_partner:
        #     partner.partner_share = not partner.user_ids or not any(not user.share for user in partner.user_ids)