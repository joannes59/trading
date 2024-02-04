# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools, Command



class TradingQuote(models.Model):
    _name = 'trading.quote'
    _description = 'Trading quote'

    asset_id = fields.Many2one('trading.asset', string='Asset', index=True)
    source_id = fields.Many2one('trading.source', string='Source', index=True)
    datetime = fields.Datetime('Date and Time', index=True)
    open_price = fields.Float('Open Price')
    close_price = fields.Float('Close Price')
    low_price = fields.Float('Low Price')
    high_price = fields.Float('High Price')
    volume = fields.Float('Volume')
