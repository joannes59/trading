# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools, Command


class Transaction(models.Model):
    _name = 'trading.transaction'
    _description = 'Trading transaction'

    asset_id = fields.Many2one('trading.asset', string='Asset')
    datetime = fields.Datetime('Date and Time')
    price = fields.Float('Price')
    amount = fields.Float('Amount')
    transaction_type = fields.Selection([
        ('buy', 'Buy'),
        ('sell', 'Sell')
    ], string='Transaction Type')
