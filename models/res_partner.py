from odoo import models, fields, api, osv, _
import logging
_logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)
import json


class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create_from_ui(self, partner):

        if('doctype' in partner):
            doctype = int(partner['doctype'])
            del partner['doctype']
            partner['doctype'] = doctype

        if('personType' in partner):
            personType = int(partner['personType'])
            del partner['personType']
            partner['personType'] = personType

        partner_id = partner.pop('id', False)
        if partner_id:  # Modifying existing partner
            self.browse(partner_id).write(partner)
        else:
            partner['lang'] = self.env.user.lang
            partner_id = self.create(partner).id

        return partner_id
