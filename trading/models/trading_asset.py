# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools, Command


class TradingAsset(models.Model):
    _name = 'trading.asset'
    _description = 'Trading asset'

    name = fields.Char('Name')
    symbol = fields.Char('Symbol')
    description = fields.Text('Description')
    asset_type = fields.Selection([
        ('cryptocurrency', 'Cryptocurrency'),
        ('currency', 'Currency'),
        ('commodity', 'Commodity')
    ], string='Type')

