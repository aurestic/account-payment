# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#    Copyright (C) 2016 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Source Document in Customer Payments",
    'version': '8.0.1.0.0',
    'category': 'Accounting & Finance',
    'author': (
        'Agile Business Group sagl,'
        'Savoir-faire linux,'
        'Odoo Community Association'
    ),
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": ['account_voucher'],
    "data": [
        'views/account_voucher.xml',
    ],
    "demo": [],
    "active": False,
    "installable": True
}
