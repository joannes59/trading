# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools, Command


class DataSource(models.Model):
    _name = 'trading.source'
    _description = 'Trading source of data'

    name = fields.Char('Name')
    description = fields.Text('Description')
